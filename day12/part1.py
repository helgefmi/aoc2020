#!/usr/bin/env python3
import pytest


def parse_lines(lines):
    for line in lines:
        yield line[0], int(line[1:])


INSTR_TO_DIR = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}

ROTATIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def rotate(facing, direction, amount):
    i = ROTATIONS.index(facing)
    return ROTATIONS[(i + direction * amount) % 4]


def move(pos, dir, amount=1):
    return (pos[0] + dir[0] * amount, pos[1] + dir[1] * amount)


def compute(cts: str):
    instructions = parse_lines(cts.splitlines())

    pos = (0, 0)
    facing = (1, 0)
    for instr, amount in instructions:
        if instr in INSTR_TO_DIR:
            pos = move(pos, INSTR_TO_DIR[instr], amount)
        elif instr == 'F':
            pos = move(pos, facing, amount)
        else:
            dir = -1 if instr == 'L' else 1
            facing = rotate(facing, dir, amount // 90)

    return abs(pos[0]) + abs(pos[1])


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ("F10\nN3\nF7\nR90\nF11", 25),
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
