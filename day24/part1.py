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


def compute(cts):
    grid = defaultdict(int)
    for line in cts.splitlines():
        coord = line_to_coord(line)
        grid[coord] = 1 - grid[coord]
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
    assert line_to_coord('esew') == (5, 10)
    assert line_to_coord('nwwswee') == (0, 0)
    assert compute(TEST) == 10


def main():
    with open('input.txt', 'r') as f:
        cts = f.read()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
