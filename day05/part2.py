#!/usr/bin/env python3
import pytest


def to_binary(s):
    trans = s.maketrans(
        {
            'F': '0',
            'B': '1',
            'L': '0',
            'R': '1',
        }
    )

    return int(s.translate(trans), 2)


def get_seat_id(s):
    row = to_binary(s[:7])
    column = to_binary(s[7:])
    return row * 8 + column


def compute(cts: str):
    seat_ids = set(map(get_seat_id, cts.splitlines()))
    for seat_id in range(min(seat_ids), max(seat_ids)):
        if seat_id not in seat_ids and seat_id + 1 in seat_ids:
            return seat_id


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820),
    ],
)
def test_compute(input_str, expected) -> None:
    assert get_seat_id(input_str) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
