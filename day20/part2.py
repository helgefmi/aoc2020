#!/usr/bin/env python3
from collections import Counter


class Dir:
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3

    OPPOSITES = [
        (Left, Right),
        (Top, Bottom),
        (Right, Left),
        (Bottom, Top),
    ]


class Tile:
    def __init__(self, tile_id, pixels):
        self.tile_id = tile_id
        self.pixels = pixels
        self.neighbors = [None] * 4
        self.size = len(pixels[0])

    def __str__(self):
        rows = [f'Tile {self.tile_id}:'] + self.pixels
        return '\n'.join(rows)

    def __repr__(self):
        return str(self.tile_id)

    def rotate(self, closed=None):
        closed = closed or set()

        if self in closed:
            return

        closed.add(self)

        new_pixels = []
        for x in range(self.size):
            new_row = ''.join(
                self.pixels[y][self.size - x - 1] for y in range(self.size)
            )
            new_pixels.append(new_row)
        self.pixels = new_pixels

        self.neighbors.append(self.neighbors.pop(0))

        for other in self.neighbors:
            if other:
                other.rotate(closed)

    def flip(self, closed=None):
        closed = closed or set()

        if self in closed:
            return

        closed.add(self)

        self.pixels.reverse()

        self.neighbors[Dir.Top], self.neighbors[Dir.Bottom] = (
            self.neighbors[Dir.Bottom],
            self.neighbors[Dir.Top],
        )

        for other in self.neighbors:
            if other:
                other.flip(closed)

    @property
    def borders(self):
        left = right = ''
        for n in range(10):
            left += self.pixels[n][0]
            right += self.pixels[n][-1]

        return [left, self.pixels[0], right, self.pixels[-1]]

    def match(self, other):
        for _ in range(2):
            for _ in range(4):
                for my_dir, other_dir in Dir.OPPOSITES:
                    if self.borders[my_dir] == other.borders[other_dir]:
                        self.neighbors[my_dir] = other
                        other.neighbors[other_dir] = self
                        return
                other.rotate()
            other.flip()


def parse_tiles(cts):
    tiles = []

    for tile_str in cts.split('\n\n'):
        lines = tile_str.splitlines()

        header, pixels = lines[0], lines[1:]
        tile_id = int(header[5:-1])

        tiles.append(Tile(tile_id, pixels))

    return tiles


def produce_image_pixels(corner_tile):
    ret = []

    y_tile = corner_tile
    while y_tile:
        x_tile = y_tile

        row = []
        while x_tile:
            row.append([col[1:-1] for col in x_tile.pixels[1:-1]])
            x_tile = x_tile.neighbors[Dir.Right]

        for zipped_line in zip(*row):
            ret.append(''.join(zipped_line))

        y_tile = y_tile.neighbors[Dir.Bottom]

    return ret


SEA_MONSTER_PATTERN = """\
..................#.
#....##....##....###
.#..#..#..#..#..#...
"""


def find_sea_monsters(pixels):
    sea_monster_lines = SEA_MONSTER_PATTERN.splitlines()
    pattern_indices = []
    for line in sea_monster_lines:
        pattern_indices.append([i for i, c in enumerate(line) if c == '#'])

    num_sea_monsters = 0
    for rows in zip(pixels, pixels[1:], pixels[2:]):
        for col_start in range(len(rows[0]) - len(sea_monster_lines[0])):
            for row_n, indices in enumerate(pattern_indices):
                if not all(rows[row_n][col_start + i] == '#' for i in indices):
                    break
            else:
                num_sea_monsters += 1

    if num_sea_monsters:
        counter = Counter()
        counter.update(''.join(pixels))
        num_sea_monster_tiles = len([i for indices in pattern_indices for i in indices])
        return counter['#'] - num_sea_monster_tiles * num_sea_monsters


def compute(cts):
    tiles = parse_tiles(cts)

    for n, tile in enumerate(tiles):
        for other in tiles[n + 1 :]:
            tile.match(other)

    corner_tile = None
    for tile in tiles:
        num_neighbors = len([x for x in tile.neighbors if x])
        if num_neighbors == 2:
            if tile.neighbors[Dir.Left] or tile.neighbors[Dir.Top]:
                continue
            corner_tile = tile
            break

    image_pixels = produce_image_pixels(corner_tile)
    image_tile = Tile(0, image_pixels)

    for _ in range(2):
        for _ in range(4):
            success = find_sea_monsters(image_tile.pixels)
            if success:
                return success
            image_tile.rotate()
        image_tile.flip()


def test_compute():
    with open('test.txt', 'r') as f:
        input_str = f.read().strip()

    assert compute(input_str) == 273


def main():
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
