#!/usr/bin/env python3
import pytest
import re
from collections import defaultdict


def gen_addrs(base_addr, float_indices):
    def recurse(mask, i):
        if i >= len(float_indices):
            yield base_addr | mask
        else:
            float_idx = float_indices[i]
            yield from recurse(mask, i + 1)
            yield from recurse(mask | (1 << float_idx), i + 1)

    yield from recurse(0, 0)


def execute_line(state, line):
    if line.startswith('mask = '):
        mask_str = line.split('=')[-1]
        state['mask_and'] = int(mask_str.replace('0', '1').replace('X', '0'), 2)
        state['mask_or'] = int(mask_str.replace('X', '0'), 2)
        state['float_indices'] = [
            i for i, x in enumerate(reversed(mask_str)) if x == 'X'
        ]
    else:
        base_addr, val = map(int, re.match(r'mem\[(\d+)\] = (\d+)', line).groups())

        base_addr |= state['mask_or']
        base_addr &= state['mask_and']

        for addr in gen_addrs(base_addr, state['float_indices']):
            state['mem'][addr] = val


def compute(cts: str):
    lines = cts.splitlines()

    state = {
        'mask_and': 0,
        'mask_or': 0,
        'float_indices': [],
        'mem': defaultdict(int),
    }

    for line in lines:
        execute_line(state, line)

    return sum(state['mem'].values())


TEST_INPUT = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INPUT, 208),
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
