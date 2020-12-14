"""
    Advent of Code 2020
    Day 14: Docking Data
"""

import re
from itertools import product


def read_puzzle_input(file_name):
    program = []
    pattern_mask = re.compile(r"(mask) = (.+)")
    pattern_mem = re.compile(r"mem\[(\d+)\] = (\d+)")

    for line in open(file_name, "r").read().splitlines():
        if line.startswith("mask"):
            lval, rval = pattern_mask.match(line).groups()
            program.append((lval, rval))
        elif line.startswith("mem"):
            lval, rval = pattern_mem.match(line).groups()
            program.append((int(lval), int(rval)))

    return tuple(program)


def day14_part1(program):
    mask_and, mask_or = None, None
    mem = {}
    for lval, rval in program:
        if lval == "mask":
            mask_and = int(rval.replace("X", "1"), 2)
            mask_or = int(rval.replace("X", "0"), 2)
        else:
            mem[lval] = (rval & mask_and) | mask_or

    return sum(mem.values())


def day14_part2(program):
    mask = ""
    mem = {}
    for lval, rval in program:
        if lval == "mask":
            mask = rval
        else:
            mem.update({addr: rval for addr in gen(mask, lval)})

    return sum(mem.values())


# def gen(mask, addr):
#     result = [""]
#     other = bin(addr)[2:].zfill(len(mask))
#     for i, c in enumerate(mask):
#         new_res = []
#         for s in result:
#             if c != "X":
#                 new_res.append(s + c if c == "1" else s + other[i])
#             else:
#                 new_res.append(s + "0")
#                 new_res.append(s + "1")
#         result = new_res
#     return [int(s, 2) for s in result]


def gen(mask: str, addr: int) -> int:
    bits = []
    other = bin(addr)[2:].zfill(len(mask))
    for i, c in enumerate(mask):
        if c != "X":
            bits.append(c if c == "1" else other[i])
        else:
            bits.append("01")

    yield from (int(''.join(s), 2) for s in product(*bits))



# Part 1
print(
    "Execute the initialization program. What is the sum of all values\
    left in memory after it completes?"
)
input_program = read_puzzle_input("data/day14.txt")
print(day14_part1(input_program))


# Part 2
print(
    "Execute the initialization program using an emulator for a version 2 decoder\
     chip. What is the sum of all values left in memory after it completes?"
)
print(day14_part2(input_program))


# Test cases
def test_day14_part1():
    assert day14_part1(read_puzzle_input("data/day14_test.txt")) == 165


def test_day14_part2():
    assert day14_part2(read_puzzle_input("data/day14_test2.txt")) == 208
