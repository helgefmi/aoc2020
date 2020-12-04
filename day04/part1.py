#!/usr/bin/env python3
import pytest


def parse_passport(s):
    return dict(entry.split(':') for entry in s.split())


def passport_is_valid(passport):
    return len(passport.keys() - ['cid']) == 7


def compute(cts: str):
    all_passports = map(parse_passport, cts.split('\n\n'))
    valid_passports = filter(passport_is_valid, all_passports)
    return len(list(valid_passports))


TEST_INPUT = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INPUT, 2),
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
