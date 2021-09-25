#!/usr/bin/env python3


class Dir:
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3

    OPPOSITES = [
        (LEFT, RIGHT),
        (TOP, BOTTOM),
        (RIGHT, LEFT),
        (BOTTOM, TOP),
    ]


class Tile:
    def __init__(self, tile_id, borders):
        self.tile_id = tile_id
        self.borders = borders
        self.neighbors = [None] * 4

    def rotate(self):
        left, top, right, bottom = self.borders
        self.borders = [top[::-1], right, bottom[::-1], left]
        self.neighbors.append(self.neighbors.pop(0))

    def flip(self):
        left, top, right, bottom = self.borders
        self.borders = [right, top[::-1], left, bottom[::-1]]

        self.neighbors[Dir.LEFT], self.neighbors[Dir.RIGHT] = (
            self.neighbors[Dir.RIGHT],
            self.neighbors[Dir.LEFT],
        )

    def match(self, other):
        for _ in range(2):
            for _ in range(4):
                for my_dir, other_dir in Dir.OPPOSITES:
                    if self.borders[my_dir] == other.borders[other_dir]:
                        self.neighbors[my_dir] = other
                        other.neighbors[other_dir] = self
                        return
                self.rotate()
            self.flip()


def parse_tiles(cts):
    tiles = []

    for tile_str in cts.split('\n\n'):
        lines = tile_str.splitlines()

        header = lines.pop(0)
        tile_id = int(header[5:-1])

        left = right = ''
        for n in range(10):
            left += lines[n][0]
            right += lines[n][-1]

        tiles.append(Tile(tile_id, [left, lines[0], right, lines[-1]]))

    return tiles


def compute(cts):
    tiles = parse_tiles(cts)

    for n, tile in enumerate(tiles):
        for other in tiles[n + 1 :]:
            tile.match(other)

    ret = 1
    for tile in tiles:
        num_neighbors = len([x for x in tile.neighbors if x])
        if num_neighbors == 2:
            ret *= tile.tile_id
    return ret


def test_compute():
    with open('test.txt', 'r') as f:
        input_str = f.read().strip()

    assert compute(input_str) == 20899048083289


def main():
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
