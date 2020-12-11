#!/usr/bin/env python3
import pytest

from collections import Counter


def compute(cts: str):
    numbers = sorted(map(int, cts.splitlines()))
    counter = Counter(n2 - n1 for n1, n2 in zip(numbers, numbers[1:]))
    return (counter[1] + 1) * (counter[3] + 1)


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ("16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4", 7 * 5),
        (
            "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n"
            "2\n34\n10\n3",
            22 * 10,
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
