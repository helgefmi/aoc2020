#!/usr/bin/env python3
from collections import defaultdict


DIRECTIONS = {
    'e': (10, 0),
    'se': (5, 10),
    'sw': (-5, 10),
    'w': (-10, 0),
    'nw': (-5, -10),
    'ne': (5, -10),
}


def line_to_coord(line):
    coord = (0, 0)
    while line:
        if line[0] in 'sn':
            s, line = line[:2], line[2:]
        else:
            s, line = line[0], line[1:]

        direction = DIRECTIONS[s]
        coord = (coord[0] + direction[0], coord[1] + direction[1])
    return coord


def iter_neighbors(coord):
    for d in DIRECTIONS.values():
        yield (coord[0] + d[0], coord[1] + d[1])


def update(grid):
    for coord in [k for k, v in grid.items() if v]:
        for ncoord in iter_neighbors(coord):
            grid[ncoord]

    to_flip = set()
    for coord, is_black in list(grid.items()):
        black_neighbors = sum(grid[ncoord] for ncoord in iter_neighbors(coord))

        if is_black and black_neighbors not in [1, 2]:
            to_flip.add(coord)
        elif not is_black and black_neighbors == 2:
            to_flip.add(coord)

    for coord in to_flip:
        grid[coord] = 1 - grid[coord]


def compute(cts):
    grid = defaultdict(int)
    for line in cts.splitlines():
        coord = line_to_coord(line)
        grid[coord] = 1 - grid[coord]

    for _ in range(100):
        update(grid)

    return sum(grid.values())


TEST = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
""".strip()


def test_compute():
    assert compute(TEST) == 2208


def main():
    with open('input.txt', 'r') as f:
        cts = f.read()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
