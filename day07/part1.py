#!/usr/bin/env python3
import pytest
from collections import defaultdict


def parse_lines(cts):
    child_to_parent_map = defaultdict(set)

    for line in cts.splitlines():
        parent_color, rest = line.split(' bags contain ')

        for child in rest.split(', '):
            child_num, child_rest = child.split(' ', 1)
            child_color = child_rest.rsplit(' ', 1)[0]
            child_to_parent_map[child_color].add(parent_color)

    return child_to_parent_map


def compute(cts: str):
    child_to_parent_map = parse_lines(cts)

    open_nodes = set(['shiny gold'])
    visited = set()
    while open_nodes:
        bag_color = open_nodes.pop()
        for parent_color in child_to_parent_map[bag_color]:
            visited.add(parent_color)
            open_nodes.add(parent_color)

    return len(visited)


TEST_INPUT = """
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
        (TEST_INPUT, 4),
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
