#!/usr/bin/env python3
import pytest
from itertools import count


def solve(bus_ids, n_start=1, n_multiple=1):
    max_offset, max_bus_id = bus_ids.pop(0)

    for n in count(n_start, n_multiple):
        if n == n_start:
            continue
        test = n * max_bus_id - max_offset
        for offset, bus_id in bus_ids:
            if (test + offset) % bus_id != 0:
                break
        else:
            break

    return n, n * max_bus_id - max_offset


def compute(line: str):
    """
    If the data set is [a, b, c, ..], we start by solving for [a, b], then use the solution of that to more quickly
    find the solution for [a, b, c], repeating this until we've solved the whole thing.
    """
    bus_ids = [(i, int(x)) for i, x in enumerate(line.split(',')) if x != 'x']

    n_multiple = 1
    n_start = 0
    # Iterate through [[a, b], [a, b, c], [a, b, c, d], ..]
    for i in range(2, len(bus_ids) + 1):
        # Find the two first solutions
        n, res = solve(bus_ids[:i], n_start, n_multiple)
        n2, res2 = solve(bus_ids[:i], n, n_multiple)

        # Use the first two solutions to know which multiple of n can be used to solve the next step,
        # and from which n to start from.
        n_multiple = n2 - n
        n_start = n
    return res


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ("17,x,13,19", 3417),
        ("67,7,59,61", 754018),
        ("67,x,7,59,61", 779210),
        ("67,7,x,59,61", 1261476),
        ("1789,37,47,1889", 1202161486),
    ],
)
def test_compute(input_str, expected) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts.splitlines()[1]))

    return 0


if __name__ == '__main__':
    exit(main())
