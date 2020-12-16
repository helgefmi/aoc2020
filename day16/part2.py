#!/usr/bin/env python3
import re
from collections import defaultdict


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


def is_valid(ticket, rules):
    for value in ticket:
        if not any(value in valid_values for valid_values in rules.values()):
            return False
    return True


def find_possible_rules(tickets, rules):
    possible_rules = defaultdict(set)

    for field in range(len(tickets[0])):
        for rule, valid_values in rules.items():
            if all(ticket[field] in valid_values for ticket in tickets):
                possible_rules[field].add(rule)

    return possible_rules


def get_rules_map(tickets, possible_rules):
    matching_rules = {}

    num_fields = len(tickets[0])

    def recurse(field=0):
        if field == num_fields:
            return True

        for rule in possible_rules[field]:
            if rule not in matching_rules:
                matching_rules[rule] = field
                if recurse(field + 1):
                    return True
                matching_rules.pop(rule)

    recurse()
    return matching_rules


def compute(cts: str):
    sections = cts.split('\n\n')

    rules = parse_rules(sections[0])
    your_ticket = parse_tickets(sections[1])[0]
    tickets = parse_tickets(sections[2])

    valid_tickets = [ticket for ticket in tickets if is_valid(ticket, rules)]
    possible_rules = find_possible_rules(valid_tickets, rules)
    matching_rules = get_rules_map(valid_tickets, possible_rules)

    ret = 1
    for rule, field in matching_rules.items():
        if rule.startswith('departure'):
            ret *= your_ticket[field]
    return ret


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
