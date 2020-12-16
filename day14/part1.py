#!/usr/bin/env python3
import pytest
import re
from collections import defaultdict


def execute_line(state, line):
    if line.startswith('mask = '):
        mask_str = line.split('=')[-1]
        state['mask_or'] = int(mask_str.replace('X', '0'), 2)
        state['mask_and'] = int(mask_str.replace('X', '1'), 2)
    else:
        addr, val = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
        state['mem'][int(addr)] = (int(val) & state['mask_and']) | state['mask_or']


def compute(cts: str):
    lines = cts.splitlines()

    state = {
        'mask_and': 0,
        'mask_or': 0,
        'mem': defaultdict(int),
    }

    for line in lines:
        execute_line(state, line)

    return sum(state['mem'].values())


TEST_INPUT = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INPUT, 165),
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
