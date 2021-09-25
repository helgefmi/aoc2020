#!/usr/bin/env python3
import pytest
import re


def parse_rules(rules_dict):
    ret = {}

    def recurse(i):
        if i not in ret:
            criteria = rules_dict[i]

            if criteria.startswith('"'):
                ret[i] = criteria[1]
            else:
                re_parts = []
                for part in criteria.split(' | '):
                    re_part = ''.join(map(recurse, part.split()))
                    re_parts.append(re_part)
                ret[i] = '(' + '|'.join(re_parts) + ')'

        return ret[i]

    recurse('0')

    return ret


def compute(cts: str):
    rules_str, messages = cts.split('\n\n')

    rules_dict = {}
    for rule_str in rules_str.splitlines():
        rule_idx, criteria = rule_str.split(': ')
        rules_dict[rule_idx] = criteria

    rules = parse_rules(rules_dict)

    rule_0 = re.compile('^' + rules['0'] + '$')

    c = 0
    for message in messages.splitlines():
        if rule_0.match(message):
            c += 1
    return c


TEST_INPUT = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INPUT, 2),
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
