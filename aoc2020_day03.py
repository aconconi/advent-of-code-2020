"""
    Advent of Code 2020
    Day 03: Toboggan Trajectory
"""

from math import prod


# def count_trees(data, right, down):
#     width = len(data[0])
#     height = len(data)
#     trees = 0
#     for i in range(0, height, down):
#         j = (i // down * right) % width
#         if data[i][j] == "#":
#             trees += 1
#     return trees


# def count_trees(data, right, down):
#     return sum(1 for i, row in enumerate(data[::down]) if row[(i * right) % len(row)] == "#")


def ring_gen(size, step):
    n = 0
    while True:
        yield n
        n = (n + step) % size


def count_trees(data, right, down):
    width = len(data[0])
    height = len(data)
    return sum(
        1
        for row, col in zip(range(0, height, down), ring_gen(width, right))
        if data[row][col] == "#"
    )


def day03_part1(data):
    return count_trees(data, 3, 1)


def day03_part2(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod(count_trees(data, right, down) for right, down in slopes)


# read input file into lines
with open("data/day03.txt", "r") as data_file:
    lines = data_file.read().splitlines()

# Part 1 solution
print("Starting at the top-left corner of your map and following a slope\
       of right 3 and down 1, how many trees would you encounter?")
print(day03_part1(lines))  # Correct answer is 216

# Part 2 solution
print("What do you get if you multiply together the number of trees \
       encountered on each of the listed slopes?")
print(day03_part2(lines))  # Correct answer is 6708199680


# Test case
test_case = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_day03_part1():
    assert day03_part1(test_case) == 7


def test_day03_part2():
    assert day03_part2(test_case) == 336
