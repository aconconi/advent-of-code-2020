"""
    Advent of Code 2020
    Day 11: Seating System
"""


OCCUPIED = "#"
FREE = "L"
FLOOR = "."
DELTAS = [(0, -1), (0, +1), (-1, 0), (+1, 0), (-1, -1), (-1, +1), (+1, -1), (+1, +1)]


def read_puzzle_input(file_name):
    """read file as list of lines"""
    return open(file_name, "r").read().splitlines()


class Grid(dict):
    def __init__(self, data):
        self.max_col = len(data[0])
        self.max_row = len(data)

        super().__init__(
            ((row, col), data[row][col])
            for row in range(self.max_row)
            for col in range(self.max_col)
        )

    def __missing__(self, key):
        return None


def solve(data, f_count, threshold):
    grid = Grid(data)

    while True:
        # apply evolution rules and track changes
        changes = set()
        for pos in grid:
            if grid[pos] == FLOOR:
                continue
            neighbors = f_count(grid, pos)
            if grid[pos] == FREE and neighbors == 0:
                changes.add((pos, OCCUPIED))
            elif grid[pos] == OCCUPIED and neighbors >= threshold:
                changes.add((pos, FREE))

        if not changes:
            # equilibrium reached, return total number of occupied seats
            return sum(c == OCCUPIED for c in grid.values())
        else:
            # commit changes to grid
            for pos, cell in changes:
                grid[pos] = cell


def day11_part1(data):
    def part1_counter(grid, pos):
        row, col = pos
        return sum(grid[(row + dr, col + dc)] == OCCUPIED for dr, dc in DELTAS)

    return solve(data, part1_counter, 4)


def day11_part2(data):
    def beam(grid, pos, inc):
        row, col = pos
        while True:
            dr, dc = inc
            row += dr
            col += dc
            if not grid[(row, col)]:
                return False
            if grid[(row, col)] == OCCUPIED:
                return True
            if grid[(row, col)] == FREE:
                return False

    def part2_counter(grid, pos):
        return sum(beam(grid, pos, inc) for inc in DELTAS)

    return solve(data, part2_counter, 5)


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
