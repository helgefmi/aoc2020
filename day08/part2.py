#!/usr/bin/env python3
import pytest


class InfiniteLoopDetected(Exception):
    pass


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
    while pc < len(program):
        if pc in visited:
            raise InfiniteLoopDetected()
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


def create_modified_programs(original_program):
    for i, (opcode, immediate) in enumerate(original_program):
        if opcode in ['jmp', 'nop']:
            program = original_program[:]
            program[i] = ('nop' if opcode == 'jmp' else 'jmp', immediate)
            yield program


def compute(cts: str):
    original_program = parse_program(cts)

    for program in create_modified_programs(original_program):
        try:
            return run_program(program)
        except InfiniteLoopDetected:
            pass


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
        (TEST_INPUT, 8),
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
