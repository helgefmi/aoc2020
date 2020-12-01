#!/usr/bin/env python3
from itertools import combinations_with_replacement


def compute(cts: str):
    numbers = [int(line) for line in cts.splitlines()]
    for n1, n2 in combinations_with_replacement(numbers, 2):
        if n1 + n2 == 2020:
            return n1 * n2


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
