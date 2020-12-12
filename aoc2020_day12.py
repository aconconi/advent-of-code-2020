"""
    Advent of Code 2020
    Day 12: Rain Risk
"""

from collections import deque


DIRS = {"N": (0, +1), "S": (0, -1), "E": (+1, 0), "W": (-1, 0)}
ROTS = {"L": 1, "R": -1}


def read_puzzle_input(file_name):
    with open(file_name, "r") as data_file:
        return [(line[0], int(line[1:])) for line in data_file.read().splitlines()]

def day12_part1(data):
    x, y = 0, 0
    direction = deque(["E", "S", "W", "N"])
    for inst, arg in data:
        if inst in DIRS:
            dx, dy = DIRS[inst]
            x += dx * arg
            y += dy * arg
        elif inst in ROTS:
            direction.rotate(ROTS[inst] * arg // 90)
        elif inst == "F":
            dx, dy = DIRS[direction[0]]
            x += dx * arg
            y += dy * arg

    return abs(x) + abs(y)


def rotate_left(x, y):
    return (-y, x)


def rotate_right(x, y):
    return (y, -x)


def day12_part2(data):
    x, y = 0, 0
    wx, wy = 10, 1
    for inst, arg in data:
        if inst in DIRS:
            dx, dy = DIRS[inst]
            wx += dx * arg
            wy += dy * arg
        elif inst in ROTS:
            for _ in range(arg % 360 // 90):
                wx, wy = rotate_left(wx, wy) if inst == "L" else rotate_right(wx, wy)
        elif inst == "F":
            x += wx * arg
            y += wy * arg

    return abs(x) + abs(y)


# Part 1
input_data = read_puzzle_input("data/day12.txt")
print("Part 1: What is the Manhattan distance between that location and the ship's starting position?")
print(day12_part1(input_data))  # Correct answer is 820

# Part 2
print("Part 2: What is the Manhattan distance between that location and the ship's starting position?")
print(day12_part2(input_data))  # Correct answer is 66614


# Test cases
test_data = read_puzzle_input("data/day12_test.txt")

def test_day12_part1():
    assert day12_part1(test_data) == 25

def test_day12_part2():
    assert day12_part2(test_data) == 286
