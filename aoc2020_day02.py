"""
    Advent of Code 2020
    Day 02: Password Philosophy
"""

import re


def day02_part1(data):
    valid = 0
    for z in data:
        low, high, char, password = re.split("-|: | ", z)
        # Alternative version using pattern matching
        # low, high, char, password = re.match("(\d*)-(\d*) (\w): (\w*)", z).groups()
        if int(low) <= password.count(char) <= int(high):
            valid += 1

    return valid


def day02_part2(data):
    valid = 0
    for z in data:
        a, b, char, password = re.split("-|: | ", z)
        p1 = password[int(a) - 1]
        p2 = password[int(b) - 1]
        if char in p1 + p2 and p1 != p2:
            valid += 1
    return valid


# read input file into lines
with open("data/day02.txt", "r") as data_file:
    lines = data_file.read().splitlines()

# Part 1 solution
print("How many passwords are valid according to their policies?")
print(day02_part1(lines))  # 493

# Part 2 solution
print("How many passwords are valid according to the new interpretation of the policies?")
print(day02_part2(lines))  # 593


# Test cases
test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def test_day02_part1():
    assert day02_part1(test_input) == 2


def test_day02_part2():
    assert day02_part2(test_input) == 1
