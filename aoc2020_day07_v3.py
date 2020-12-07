"""
    Advent of Code 2020
    Day 07: Handy Haversacks
"""

import re
from collections import defaultdict

with open("data/day07.txt", "r") as data_file:
    input_data = data_file.read().splitlines()

graph = {}

for line in input_data:
    color = re.match(r"(.+?) bags", line).group(1)
    contained_list = re.findall(r"(\d+) (.+?) bag", line)
    graph[color] = dict((color, int(quant)) for quant, color in contained_list)


# Iterative implementation for Part 1
def day06_part1():
    queue = ["shiny gold"]
    solutions = []
    while queue:
        color = queue.pop(0)
        if color not in solutions:
            solutions.append(color)
            queue.extend([c for c in graph if color in graph[c]])
    return len(solutions) - 1


# Recursive implementation for Part 2
def day06_part2():
    def solve(color):
        return sum(
            (1 + solve(contained)) * graph[color][contained]
            for contained in graph[color]
        )

    return solve("shiny gold")


# Part 1
print("How many bag colors can eventually contain at least one shiny gold bag?")
print(day06_part1())  # Correct answer is 316

# Part 2
print("How many individual bags are required inside your single shiny gold bag?")
print(day06_part2())  # Correct answer is 11310

