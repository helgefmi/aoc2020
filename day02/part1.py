#!/usr/bin/env python3
from collections import Counter


def parse_line(line):
    policy, password = line.split(': ')
    policy_range, policy_char = policy.split(' ')
    policy_low, policy_high = map(int, policy_range.split('-'))
    return {
        'password': password,
        'policy_range': range(policy_low, policy_high + 1),
        'policy_char': policy_char,
    }


def check_entry(entry):
    counter = Counter(entry['password'])
    return counter[entry['policy_char']] in entry['policy_range']


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
