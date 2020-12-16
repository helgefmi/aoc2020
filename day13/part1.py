#!/usr/bin/env python3
import math
import pytest


def compute(cts: str):
    lines = cts.splitlines()

    earliest_departure = int(lines.pop(0))
    bus_ids = [int(x) for x in lines.pop(0).split(',') if x != 'x']

    best_candidate = (math.inf, 0)

    for bus_id in bus_ids:
        minutes_to_wait = earliest_departure % bus_id
        minutes_to_wait = (-1 * minutes_to_wait) % bus_id

        candidate = (minutes_to_wait, bus_id)
        if candidate < best_candidate:
            best_candidate = candidate

    return best_candidate[0] * best_candidate[1]


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ("939\n7,13,x,x,59,x,31,19", 295),
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
