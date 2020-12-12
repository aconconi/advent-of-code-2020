"""
    Advent of Code 2020
    Day 12: Rain Risk
"""

DIRS = {"N": (0, +1), "S": (0, -1), "E": (+1, 0), "W": (-1, 0)}
ROTATE = { 'L': lambda x, y : (-y, x), 'R': lambda x, y: (y, -x)}


def read_puzzle_input(file_name):
    with open(file_name, "r") as data_file:
        return [(line[0], int(line[1:])) for line in data_file.read().splitlines()]


def day12_part1(data):
    x, y = 0, 0
    direction = DIRS["E"]

    for inst, arg in data:
        if inst in DIRS:
            dx, dy = DIRS[inst]
            x += dx * arg
            y += dy * arg
        elif inst in ROTATE:
            for _ in range(arg % 360 // 90):
                direction = ROTATE[inst](*direction)
        elif inst == "F":
            dx, dy = direction
            x += dx * arg
            y += dy * arg

    return abs(x) + abs(y)


def day12_part2(data):
    x, y = 0, 0
    wx, wy = 10, 1

    for inst, arg in data:
        if inst in DIRS:
            dx, dy = DIRS[inst]
            wx += dx * arg
            wy += dy * arg
        elif inst in ROTATE:
            for _ in range(arg % 360 // 90):
                wx, wy = ROTATE[inst](wx, wy)
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
