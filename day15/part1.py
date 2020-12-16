#!/usr/bin/env python3
import pytest


def compute(cts: str):
    history = [int(x) for x in cts.split(',')]
    history.reverse()

    for _ in range(2020 - len(history)):
        val = history[0]
        if val not in history[1:]:
            history.insert(0, 0)
        else:
            last_spoken = history.index(val, 1)
            history.insert(0, last_spoken)

    return history[0]


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ('0,3,6', 436),
        ('1,3,2', 1),
        ('2,1,3', 10),
        ('1,2,3', 27),
        ('2,3,1', 78),
        ('3,2,1', 438),
        ('3,1,2', 1836),
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
