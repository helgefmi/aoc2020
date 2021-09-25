#!/usr/bin/env python3
from itertools import count, islice


def transforms(subject_number):
    value = 1
    for n in count(1):
        value = value * subject_number
        value = value % 20201227
        yield n, value


def transform(subject_number, loop_size):
    sliced = islice(transforms(subject_number), loop_size - 1)
    return next(sliced)[1]


def compute(cts):
    pub_keys = [int(n) for n in cts.splitlines()]

    for loop_size, result in transforms(7):
        if result in pub_keys:
            break

    idx = pub_keys.index(result)
    return transform(pub_keys[1 - idx], loop_size)


TEST = """
5764801
17807724
""".strip()


def test_compute():
    assert compute(TEST) == 14897079


def main():
    with open('input.txt', 'r') as f:
        cts = f.read()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
