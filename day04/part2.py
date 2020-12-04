#!/usr/bin/env python3
import pytest
import re

#  byr (Birth Year) - four digits; at least 1920 and at most 2002.
#  iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#  eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#  hgt (Height) - a number followed by either cm or in:
#      If cm, the number must be at least 150 and at most 193.
#      If in, the number must be at least 59 and at most 76.
#  hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#  ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#  pid (Passport ID) - a nine-digit number, including leading zeroes.
#  cid (Country ID) - ignored, missing or not.


def parse_passport(s):
    return dict(entry.split(':') for entry in s.split())


def passport_is_valid(passport):
    ranges = {
        'byr': range(1920, 2002 + 1),
        'iyr': range(2010, 2020 + 1),
        'eyr': range(2020, 2030 + 1),
    }

    unit_ranges = {
        'hgt': {
            'cm': range(150, 193 + 1),
            'in': range(59, 76 + 1),
        }
    }

    rules = {
        'byr': r'(\d{4})',
        'iyr': r'(\d{4})',
        'eyr': r'(\d{4})',
        'hgt': r'(\d+)(cm|in)',
        'hcl': r'#[0-9a-f]{6}',
        'ecl': r'(amb|blu|brn|gry|grn|hzl|oth)',
        'pid': r'\d{9}',
    }

    for key, rule in rules.items():
        if key not in passport:
            return False

        match = re.match(f'^{rule}$', passport[key])
        if not match:
            return False

        if key in ranges:
            value = match.group(1)
            if int(value) not in ranges[key]:
                return False

        if key in unit_ranges:
            value, unit = match.groups(1)
            if int(value) not in unit_ranges[key][unit]:
                return False

    return True


def compute(cts: str):
    all_passports = map(parse_passport, cts.split('\n\n'))
    valid_passports = filter(passport_is_valid, all_passports)
    return len(list(valid_passports))


TEST_INVALID_PASSPORTS = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
""".strip()


TEST_VALID_PASSPORTS = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INVALID_PASSPORTS, 0),
        (TEST_VALID_PASSPORTS, 4),
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
