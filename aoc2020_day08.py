"""
    Advent of Code 2020
    Day 08: Handheld Halting
"""

from collections import Counter

def read_puzzle_input(file_name):
    '''Reads program from file and returns a program as list of (instruction, argument) tuples.'''
    puzzle_input = open(file_name, "r").read().splitlines()
    return [(line.split()[0], int(line.split()[1])) for line in puzzle_input]


def safe_run(program):
    '''Runs the program, returns (True, acc) if it terminates, (False, acc) if a loop is detected.'''
    reps = set()
    pc = 0
    acc = 0
    while pc < len(program):
        instr, arg = program[pc]
        if pc in reps:
            return (False, acc)
        else:
            reps.add(pc)

        if instr == "acc":
            acc += arg
            pc += 1
        elif instr == "jmp":
            pc += arg
        elif instr == "nop":
            pc += 1

    return (True, acc)


def day08_part1(program):
    _, acc = safe_run(program)
    return acc


def day08_part2(program):
    # Try a first run withount changing anything because maybe the program is not corrupted at all.
    halts, acc = safe_run(program)
    if halts:
        return acc

    # For each possible program line that can be fixed, apply fix and attempt a safe run.
    FIX = {"nop": "jmp", "jmp": "nop"}
    for i, (instr, arg) in enumerate(program):
        if instr in FIX:
            fixed_program = program[:i] + [(FIX[instr], arg)] + program[i + 1 :]
            halts, acc = safe_run(fixed_program)
            if halts:
                # the fix worked!
                return acc

    # If we get here, something is wrong.
    raise Exception("Could not find a fix for this program.")


# Part 1
input_program = read_puzzle_input("data/day08.txt")
print( "Immediately before any instruction is executed a second time, what value is in the accumulator?")
print(day08_part1(input_program))  # Correct answer is 2058.

# Part 2
print("What is the value of the accumulator after the program terminates?")
print(day08_part2(input_program))  # Correct answer is 1000.


# Test cases
def test_day08_part1():
    test_program = read_puzzle_input("data/day08_test.txt")
    assert day08_part1(test_program) == 5

def test_day08_part2():
    test_program = read_puzzle_input("data/day08_test.txt")
    assert day08_part2(test_program) == 8
