#!/usr/bin/env python3
import pytest
from collections import Counter


def compute(cts: str):
    ret = 0
    for group in cts.split('\n\n'):
        answers = group.split()
        counter = Counter(''.join(answers))
        ret += sum(num == len(answers) for num in counter.values())
    return ret


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ("abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb", 6),
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
