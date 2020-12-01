"""
    Advent of Code 2020
    Day 01: Report Repair
"""

# read input file into lines
with open("data/day01.dat", "r") as data_file:
    lines = data_file.read().splitlines()

data = [int(x) for x in lines]


# brute force solution
# def day01_part01():
#     return next(i * j for i in data for j in data if i + j == 2020)

# def day01_part02():
#     return next(i * j * k for i in data for j in data for k in data if i + j + k == 2020)


# better solution leveraging data sort
data.sort()
min_n = min(data)

def day01_part01():
    for i in data:
        for j in data:
            if i + j == 2020:
                return i * j
            elif i + j > 2020:
                break
    return None


def day01_part02():
    for i in data:
        for j in data:
            if i + j > 2020:
                break

            for k in data:
                if i + j + k == 2020:
                    return i * j * k
                elif i + j + k > 2020:
                    break
    return None


# Part 1
print(day01_part01())  # Correct answer is 1007104

# Part 2
print(day01_part02())  # Correct answer is 18847752
