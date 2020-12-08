#!/usr/bin/env python3
import pytest
from collections import defaultdict


def parse_lines(cts):
    parent_to_child_map = defaultdict(set)

    for line in cts.splitlines():
        parent_color, rest = line.split(' bags contain ')

        for child in rest.split(', '):
            child_num, child_rest = child.split(' ', 1)
            if child_num == 'no':
                continue
            child_color = child_rest.rsplit(' ', 1)[0]
            parent_to_child_map[parent_color].add((int(child_num), child_color))

    return parent_to_child_map


def compute(cts: str):
    parent_to_child_map = parse_lines(cts)

    need = set([(1, 'shiny gold')])
    have = defaultdict(int)
    while need:
        num, color = need.pop()
        for child_num, child_color in parent_to_child_map[color]:
            have[child_color] += num * child_num
            need.add((child_num * num, child_color))

    return sum(v for k, v in have.items())


TEST_INPUT_1 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".strip()

TEST_INPUT_2 = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INPUT_1, 126),
        (TEST_INPUT_2, 32),
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
