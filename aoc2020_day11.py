"""
    Advent of Code 2020
    Day 11: Seating System
"""

from typing import Collection


from collections import defaultdict


def read_puzzle_input(file_name):
    """read file as list of rows and create a grid as list of list of characters"""
    return open(file_name, "r").read().splitlines()


test_data = read_puzzle_input("data/day11_test.txt")
input_data = read_puzzle_input("data/day11.txt")

OCCUPIED = "#"
FREE = "L"
deltas = [
    (0, -1),
    (0, +1),
    (-1, 0),
    (+1, 0),
    (-1, -1),
    (-1, +1),
    (+1, -1),
    (+1, +1),
]




def day11_part1(data):
    max_col = len(data[0])
    max_row = len(data)

    adjacency = {
        (row, col): [
            (row + dr, col + dc)
            for dr, dc in deltas
            if 0 <= row + dr < max_row and 0 <= col + dc < max_col
        ]
        for col in range(max_col)
        for row in range(max_row)
    }

    grid = {
        (row, col): data[row][col] for row in range(max_row) for col in range(max_col)
    }

    while True:
        changes = []
        for pos in grid:
            neighbors = sum(grid[z] == OCCUPIED for z in adjacency[pos])
            if grid[pos] == FREE and neighbors == 0:
                changes.append((pos, OCCUPIED))
            elif grid[pos] == OCCUPIED and neighbors >= 4:
                changes.append((pos, FREE))

        if not changes:
            return sum(c == OCCUPIED for c in grid.values())
        else:
            for pos, cell in changes:
                grid[pos] = cell


def day11_part2(data):
    max_col = len(data[0])
    max_row = len(data)

    def beam(grid, pos, dir):
        row, col = pos
        dr, dc = dir
        while True:
            row += dr
            col += dc
            if not (0 <= row < max_row and 0 <= col < max_col):
                return False
            if grid[(row, col)] == OCCUPIED:
                return True
            if grid[(row, col)] == FREE:
                return False

    gen = {
        (row, col): data[row][col] for row in range(max_row) for col in range(max_col)
    }

    while True:
        changes = set()
        for pos in gen:
            neighbors = sum(beam(gen, pos, d) for d in deltas)
            if gen[pos] == FREE and neighbors == 0:
                changes.add((pos, OCCUPIED))
            elif gen[pos] == OCCUPIED and neighbors >= 5:
                changes.add((pos, FREE))

        if not changes:
            return sum(c == OCCUPIED for c in gen.values())
        else:
            for pos, cell in changes:
                gen[pos] = cell


# def solve(data, f_count, threshold):



# Part 1
print(
    "Simulate your seating area by applying the seating rules repeatedly\
    until no seats change state. How many seats end up occupied?"
)
print(day11_part1(input_data))

# Part 2
print(
    "Given the new visibility method and the rule change for occupied seats\
    becoming empty, once equilibrium is reached, how many seats end up occupied?"
)
print(day11_part2(input_data))  # Correct answer is 2149



# Test cases
test_data = read_puzzle_input("data/day11_test.txt")

def test_day11_part1():
    assert day11_part1(test_data) == 37

def test_day11_part2():
    assert day11_part2(test_data) == 26
