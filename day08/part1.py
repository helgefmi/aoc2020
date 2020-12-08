#!/usr/bin/env python3
import pytest


def parse_program(cts):
    program = []
    for line in cts.splitlines():
        opcode, immediate = line.split(' ')
        program.append((opcode, int(immediate)))
    return program


def run_program(program):
    acc = 0
    pc = 0
    visited = set()
    while True:
        # print(pc, acc, opcode, immediate)

        if pc in visited:
            break
        visited.add(pc)

        opcode, immediate = program[pc]
        if opcode == 'nop':
            pc += 1
        elif opcode == 'jmp':
            pc += immediate
        elif opcode == 'acc':
            acc += immediate
            pc += 1

    return acc


def compute(cts: str):
    program = parse_program(cts)

    return run_program(program)


TEST_INPUT = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()


@pytest.mark.parametrize(
    'input_str, expected',
    [
        (TEST_INPUT, 5),
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
