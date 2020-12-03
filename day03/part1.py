#!/usr/bin/env python3
import pytest


def compute(cts: str):
    area = cts.splitlines()
    height = len(area)
    width = len(area[0])

    pos = (0, 0)
    count = 0
    while pos[1] < height:
        x, y = pos
        if area[y][x % width] == '#':
            count += 1
        pos = (x + 3, y + 1)
    return count


TEST_INPUT = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INPUT, 7),
    ],
)
def test_compute(input_str, expected) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
