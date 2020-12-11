#!/usr/bin/env python3
import pytest


def find_invalid_element(numbers, preamble_length):
    for i, n in enumerate(numbers[preamble_length:]):
        relevant_numbers = numbers[i : i + preamble_length]
        candidates = [n - x for x in relevant_numbers]
        if not any(candidate in relevant_numbers for candidate in candidates):
            return n


def find_encryption_weakness(numbers, invalid_element):
    for low in range(len(numbers)):
        for high in range(low, len(numbers)):
            relevant_numbers = numbers[low:high]
            res = sum(relevant_numbers)
            if res == invalid_element:
                return min(relevant_numbers) + max(relevant_numbers)
            elif res > invalid_element:
                break


def compute(cts: str, preamble_length: int):
    numbers = list(map(int, cts.splitlines()))
    invalid_element = find_invalid_element(numbers, preamble_length)
    return find_encryption_weakness(numbers, invalid_element)


@pytest.mark.parametrize(
    'input_str, preamble_length, expected',
    [
        (
            "20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576",
            5,
            62,
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
