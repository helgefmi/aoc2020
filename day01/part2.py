#!/usr/bin/env python3
from functools import reduce
from itertools import combinations_with_replacement
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def criteria_for(numbers, num_elements, criteria=2020):
    for combination in combinations_with_replacement(numbers, num_elements):
        if sum(combination) == criteria:
            return prod(combination)


def compute(cts: str):
    numbers = [int(line) for line in cts.splitlines()]
    return criteria_for(numbers, 3)


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
