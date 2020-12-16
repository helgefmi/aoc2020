#!/usr/bin/env python3
import re


def parse_rules(rules_str):
    ret = {}
    for line in rules_str.splitlines():
        match = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line)
        key = match.group(1)
        lo1, hi1, lo2, hi2 = map(int, match.groups()[1:])
        ret[key] = set(range(lo1, hi1 + 1)) | set(range(lo2, hi2 + 1))
    return ret


def parse_tickets(tickets_str):
    ret = []
    for line in tickets_str.splitlines()[1:]:
        ret.append(list(map(int, line.split(','))))
    return ret


def compute(cts: str):
    sections = cts.split('\n\n')

    rules = parse_rules(sections[0])
    tickets = parse_tickets(sections[2])

    invalid_values = []
    for ticket in tickets:
        for value in ticket:
            if not any(value in valid_values for valid_values in rules.values()):
                invalid_values.append(value)

    return sum(invalid_values)


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
