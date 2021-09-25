#!/usr/bin/env python3
import random
import pytest


"""
This is a stupid solution. It uses random.choice() below, with 200 attempts per message. Seems to always give the right
answer, but obviously not deterministic.
"""


def parse_rules(rules_str):
    rules_dict = {}
    for rule_str in rules_str.splitlines():
        rule_idx, criteria = rule_str.split(': ')
        if criteria.startswith('"'):
            rules_dict[rule_idx] = criteria[1]
        else:
            parts = []
            for part in criteria.split(' | '):
                parts.append([x for x in part.split()])
            rules_dict[rule_idx] = parts
    return rules_dict


def matches_rules(message, rules_dict):
    def recurse(rule_idx, i=0, depth=0):
        if i == len(message):
            return True, i
        # print(f'{" " * depth}{rule_idx}: {message[:i]}')
        rule = rules_dict[rule_idx]
        if isinstance(rule, list):
            all_matches = []
            for or_branches in rule:
                total_n = 0
                for child_rule in or_branches:
                    matches, n = recurse(child_rule, i + total_n, depth + 1)
                    if not matches:
                        break
                    total_n += n
                else:
                    all_matches.append(total_n)
            if all_matches:
                return True, random.choice(all_matches)
        else:
            if i < len(message) and message[i] == rule:
                return True, 1

        return False, 0

    matches, total_n = recurse('0')
    return matches and total_n == len(message)


def update_rules(rules_dict):
    rules_dict['8'] = [['42'], ['42', '8']]
    rules_dict['11'] = [['42', '11', '31'], ['42', '31']]


def compute(cts: str):
    rules_str, messages = cts.split('\n\n')

    rules_dict = parse_rules(rules_str)
    update_rules(rules_dict)

    c = 0
    for message in messages.splitlines():
        for _ in range(200):
            if matches_rules(message, rules_dict):
                c += 1
                break
    return c


TEST_INPUT = """
0: 8 11
1: "a"
2: 1 24 | 14 4
3: 5 14 | 16 1
4: 1 1
5: 1 14 | 15 1
6: 14 14 | 1 14
7: 14 5 | 1 21
8: 42
9: 14 27 | 1 26
10: 23 14 | 28 1
11: 42 31
12: 24 14 | 19 1
13: 14 3 | 1 12
14: "b"
15: 1 | 14
16: 15 1 | 14 14
17: 14 2 | 1 7
18: 15 15
19: 14 1 | 14 14
20: 14 14 | 1 15
21: 14 1 | 1 14
22: 14 14
23: 25 1 | 22 14
24: 14 1
25: 1 1 | 1 14
26: 14 22 | 1 20
27: 1 6 | 14 18
28: 16 1
31: 14 17 | 1 13
42: 9 14 | 10 1

aaaaabbaabaaaaababaa
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INPUT, 1),
    ],
)
def test_compute(input_str, expected):
    assert compute(input_str) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
