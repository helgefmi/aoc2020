#!/usr/bin/env python3
import pytest


def get_axis_range(cubes, axis):
    coords = [cube[axis] for cube in cubes.keys()]
    return range(min(coords) - 1, max(coords) + 2)


def iterate_cubes(cubes):
    for x in get_axis_range(cubes, 0):
        for y in get_axis_range(cubes, 1):
            for z in get_axis_range(cubes, 2):
                yield x, y, z


def get_neighbors(x, y, z):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx or dy or dz:
                    yield (x + dx, y + dy, z + dz)


def tick(cubes):
    new_cubes = {}

    for x, y, z in iterate_cubes(cubes):
        active = cubes.get((x, y, z))

        num_active_neighbors = 0
        for neighbor in get_neighbors(x, y, z):
            if cubes.get(neighbor):
                num_active_neighbors += 1

        if (
            active
            and num_active_neighbors in [2, 3]
            or not active
            and num_active_neighbors == 3
        ):
            new_cubes[(x, y, z)] = True

    return new_cubes


def compute(cts: str):
    cubes = {}
    for y, line in enumerate(cts.splitlines()):
        for x, c in enumerate(line):
            cubes[(y, x, 0)] = c == '#'

    for _ in range(6):
        cubes = tick(cubes)

    return sum(1 for state in cubes.values() if state)


TEST_INPUT = """
.#.
..#
###
""".strip()


@pytest.mark.parametrize('input_str, expected', [(TEST_INPUT, 112)])
def test_compute(input_str, expected):
    assert compute(input_str) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
