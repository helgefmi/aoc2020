#!/usr/bin/env python3
import pytest


OPERATORS = {
    '*': 0,
    '+': 1,
}


def is_operator(tok):
    return tok in OPERATORS


def parse_operator_expression(lhs, tokens, min_precedence=0):
    if not tokens:
        return lhs, []

    while tokens and is_operator(tokens[0]):
        op = tokens.pop(0)
        rhs, tokens = parse_primary(tokens)
        while (
            tokens and is_operator(tokens[0]) and OPERATORS[op] < OPERATORS[tokens[0]]
        ):
            rhs, tokens = parse_operator_expression(rhs, tokens, OPERATORS[tokens[0]])
        lhs = eval(f'{lhs}{op}{rhs}')

    return lhs, tokens


def parse_expression(tokens):
    lhs, tokens = parse_primary(tokens)
    return parse_operator_expression(lhs, tokens)


def parse_primary(tokens):
    tok = tokens.pop(0)

    if not tokens:
        return tok, []

    if tok == '(':
        expr, tokens = parse_expression(tokens)
        assert tokens.pop(0) == ')'
        return expr, tokens
    elif tok.isdigit():
        return tok, tokens
    else:
        assert False, tok


def eval_line(line):
    tokens = line.replace('(', ' ( ').replace(')', ' ) ').split()
    expr, tokens = parse_expression(tokens)
    assert not tokens
    return expr


def compute(cts: str):
    s = 0
    for line in cts.splitlines():
        s += eval_line(line)
    return s


@pytest.mark.parametrize(
    'input_str, expected',
    [
        ('1 + (2 * 3) + (4 * (5 + 6))', 51),
        ('2 * 3 + (4 * 5)', 46),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
    ],
)
def test_compute(input_str, expected):
    assert eval_line(input_str) == expected


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
