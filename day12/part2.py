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


def rotate_right(pos, times):
    for _ in range(times):
        pos = (pos[1] * -1, pos[0])
    return pos


def move(pos, dir, amount=1):
    return (pos[0] + dir[0] * amount, pos[1] + dir[1] * amount)


def compute(cts: str, waypoint=(10, -1)):
    instructions = parse_lines(cts.splitlines())

    pos = (0, 0)
    for instr, amount in instructions:
        if instr in INSTR_TO_DIR:
            waypoint = move(waypoint, INSTR_TO_DIR[instr], amount)
        elif instr == 'F':
            pos = move(pos, waypoint, amount)
        else:
            dir = -1 if instr == 'L' else 1
            waypoint = rotate_right(waypoint, dir * (amount // 90) % 4)

    return abs(pos[0]) + abs(pos[1])


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ("F10\nN3\nF7\nR90\nF11", 286),
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
