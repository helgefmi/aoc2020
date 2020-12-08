#!/usr/bin/env python3
import pytest


def to_binary(s):
    trans = s.maketrans('FBLR', '0101')
    return int(s.translate(trans), 2)


def compute(cts: str):
    return max(to_binary(line) for line in cts.splitlines())


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820),
    ],
)
def test_compute(input_str, expected) -> None:
    assert to_binary(input_str) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
