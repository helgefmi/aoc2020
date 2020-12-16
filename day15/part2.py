#!/usr/bin/env python3
import pytest


def compute(cts: str, game_length):
    starting_numbers = [int(x) for x in cts.split(',')]

    history = {n: turn for turn, n in enumerate(starting_numbers, 1)}
    next_val = 0
    for turn in range(len(starting_numbers) + 1, game_length):
        if next_val not in history:
            history[next_val] = turn
            next_val = 0
        else:
            history[next_val], next_val = turn, turn - history[next_val]

    return next_val


@pytest.mark.parametrize(
    'input_str, game_length, expected',
    [
        ('0,3,6', 2020, 436),
        ('1,3,2', 2020, 1),
        ('2,1,3', 2020, 10),
        ('1,2,3', 2020, 27),
        ('2,3,1', 2020, 78),
        ('3,2,1', 2020, 438),
        ('3,1,2', 2020, 1836),
        ('0,3,6', 30000000, 175594),
        ('1,3,2', 30000000, 2578),
        ('2,1,3', 30000000, 3544142),
        ('1,2,3', 30000000, 261214),
        ('2,3,1', 30000000, 6895259),
        ('3,2,1', 30000000, 18),
        ('3,1,2', 30000000, 362),
    ],
)
def test_compute(input_str, game_length, expected) -> None:
    assert compute(input_str, game_length) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts, 30000000))

    return 0


if __name__ == '__main__':
    exit(main())
