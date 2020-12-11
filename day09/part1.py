#!/usr/bin/env python3
import pytest


def compute(cts: str, preamble_length: int):
    numbers = list(map(int, cts.splitlines()))
    for i, n in enumerate(numbers[preamble_length:]):
        relevant_numbers = numbers[i : i + preamble_length]
        candidates = [n - x for x in relevant_numbers]
        if not any(candidate in relevant_numbers for candidate in candidates):
            return n


@pytest.mark.parametrize(
    'input_str, preamble_length, expected',
    [
        (
            "20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576",
            5,
            127,
        ),
    ],
)
def test_compute(input_str, preamble_length, expected) -> None:
    assert compute(input_str, preamble_length) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts, 25))

    return 0


if __name__ == '__main__':
    exit(main())
