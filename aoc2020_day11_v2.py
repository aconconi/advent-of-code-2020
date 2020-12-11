"""
    Advent of Code 2020
    Day 11: Seating System
"""

from copy import deepcopy


OCCUPIED = "#"
FREE = "L"
FLOOR = "."
DELTAS = [(0, -1), (0, +1), (-1, 0), (+1, 0), (-1, -1), (-1, +1), (+1, -1), (+1, +1)]


def read_puzzle_input(file_name):
    """read file as list of lines"""
    return open(file_name, "r").read().splitlines()


def solve(grid, neighbors_counter, threshold):
    while True:
        # apply evolution rules and track changes
        newgrid = deepcopy(grid)

        changes = False
        # evolve each seat depending on number of occupied neighbor seats
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == FLOOR:
                    continue
                neighbours = neighbors_counter(grid, i, j)
                if cell == FREE and neighbours == 0:
                    newgrid[i][j] = OCCUPIED
                    changes = True
                elif cell == OCCUPIED and neighbours >= threshold:
                    newgrid[i][j] = FREE
                    changes = True

        if not changes:
            # equilibrium reached, return total number of occupied seats
            return sum(cell == OCCUPIED for row in grid for cell in row)
        else:
            # commit changes to grid and continue evolution
            grid = newgrid


def day11_part1(data):
    max_row = len(data)
    max_col = len(data[0])

    def part1_counter(grid, row, col):
        total = 0
        for dr, dc in DELTAS:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < max_row and 0 <= nc < max_col:
                total += 1 if grid[nr][nc] == OCCUPIED else 0
        return total

    grid = [list(line) for line in data]
    return solve(grid, part1_counter, 4)


def day11_part2(data):
    max_row = len(data)
    max_col = len(data[0])

    def part2_counter(grid, row, col):
        total = 0
        for dr, dc in DELTAS:
            nr, nc = row + dr, col + dc
            while (0 <= nr < max_row and 0 <= nc < max_col):
                if grid[nr][nc] == OCCUPIED:
                    total +=1
                if grid[nr][nc] != FLOOR:
                    break
                nr += dr
                nc += dc

        return total

    grid = [list(line) for line in data]
    return solve(grid, part2_counter, 5)


# Part 1
input_data = read_puzzle_input("data/day11.txt")
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
print(day11_part2(input_data))


# Test cases
test_data = read_puzzle_input("data/day11_test.txt")


def test_day11_part1():
    assert day11_part1(test_data) == 37


def test_day11_part2():
    assert day11_part2(test_data) == 26
