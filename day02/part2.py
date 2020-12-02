#!/usr/bin/env python3
from collections import Counter


def parse_line(line):
    policy, password = line.split(': ')
    policy_range, policy_char = policy.split(' ')
    policy_n1, policy_n2 = map(int, policy_range.split('-'))
    return {
        'password': password,
        'policy_n1': policy_n1 - 1,
        'policy_n2': policy_n2 - 1,
        'policy_char': policy_char,
    }


def check_entry(entry):
    chars_to_check = (
        entry['password'][entry['policy_n1']] + entry['password'][entry['policy_n2']]
    )
    counter = Counter(chars_to_check)
    return counter[entry['policy_char']] == 1


def compute(cts: str):
    entries = map(parse_line, cts.splitlines())
    valid_entries = filter(check_entry, entries)
    return len(list(valid_entries))


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
