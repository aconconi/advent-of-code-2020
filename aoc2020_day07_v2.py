"""
    Advent of Code 2020
    Day 07: Handy Haversacks
"""

import re
from collections import defaultdict

with open("data/day07.txt", "r") as data_file:
    input_data = data_file.read().splitlines()

contains = dict()
containers = defaultdict(lambda: [])

for line in input_data:
    container, contained = line.split(" contain ")
    container = container.replace(" bags", "")
    if contained.startswith("no other"):
        continue

    contained_list = [re.sub(r" bag.*$", "", bag) for bag in contained.split(", ")]
    for entry in contained_list:
        quant, color = entry.split(" ", 1)
        contains[(container, color)] = int(quant)
        containers[color].append(container)


# Iterative implementation for Part 1
def day06_part1():
    queue = containers["shiny gold"].copy()
    solutions = []
    while queue:
        color = queue.pop(0)
        if color not in solutions:
            solutions.append(color)
            queue.extend(containers[color])
    return len(solutions)


# Recursive implementation for Part 1
def day06_part1_recursive():
    def solve(solutions):
        if not solutions:
            return set()
        else:
            new_sols = set()
            for s in solutions:
                new_sols |= set(containers[s])
            return solutions | new_sols | solve(new_sols - solutions)

    return len(solve({"shiny gold"})) - 1


# Recursive implementation for Part 2
def day06_part2():
    def solve(color):
        return sum(
            (1 + solve(contained)) * contains[(color, contained)]
            for contained in (b for (a, b) in contains if a == color)
        )

    return solve("shiny gold")


# Part 1
print("How many bag colors can eventually contain at least one shiny gold bag?")
print(day06_part1())  # Correct answer is 316

# Part 2
print("How many individual bags are required inside your single shiny gold bag?")
print(day06_part2())  # Correct answer is 11310

# Test
assert day06_part1_recursive() == day06_part1()
