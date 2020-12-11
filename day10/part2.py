#!/usr/bin/env python3
import pytest
from functools import lru_cache


def compute(cts: str):
    numbers = [0] + list(sorted(map(int, cts.splitlines())))

    @lru_cache
    def recurse(i):
        if i == len(numbers) - 1:
            return 1
        child_is = range(i + 1, min(i + 4, len(numbers)))
        return sum(recurse(ci) for ci in child_is if numbers[ci] < numbers[i] + 4)

    return recurse(0)


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ("16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4", 8),
        (
            "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n"
            "38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3",
            19208,
        ),
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
