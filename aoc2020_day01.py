"""
    Advent of Code 2020
    Day 01: Report Repair
"""

# read input file into lines
with open("data/day01.dat", "r") as data_file:
    lines = data_file.read().splitlines()

data = [int(x) for x in lines]
data.sort()


def day01_part01():
    return next(n * (2020 - n) for n in data if 2020 - n in data)


def day01_part02():
    return next(
        i * j * (2020 - i - j)
        for i in data
        for j in (x for x in data if i + x < 2020)
        if 2020 - i - j in data
    )


# Part 1
print(day01_part01())  # Correct answer is 1007104

# Part 2
print(day01_part02())  # Correct answer is 18847752
