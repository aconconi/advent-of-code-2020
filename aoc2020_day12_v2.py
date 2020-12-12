"""
    Advent of Code 2020
    Day 12: Rain Risk
"""

DIRS = {
    "N": 0 + 1j,
    "S": 0 - 1j,
    "E": 1 + 0j,
    "W": -1 + 0j
}

ROTATE = {
    "L": lambda z: complex(-z.imag, z.real),
    "R": lambda z: complex(z.imag, -z.real),
}


def read_puzzle_input(file_name):
    with open(file_name, "r") as data_file:
        return tuple((line[0], int(line[1:])) for line in data_file.read().splitlines())


def day12_part1(data):
    position = 0 + 0j
    direction = DIRS["E"]

    for inst, arg in data:
        if inst in DIRS:
            position += DIRS[inst] * arg
        elif inst in ROTATE:
            for _ in range(arg % 360 // 90):
                direction = ROTATE[inst](direction)
        elif inst == "F":
            position += direction * arg

    return int(abs(position.real) + abs(position.imag))


def day12_part2(data):
    ship = 0 + 0j
    waypoint = 10 + 1j

    for inst, arg in data:
        if inst in DIRS:
            waypoint += DIRS[inst] * arg
        elif inst in ROTATE:
            for _ in range(arg % 360 // 90):
                waypoint = ROTATE[inst](waypoint)
        elif inst == "F":
            ship += waypoint * arg

    return int(abs(ship.real) + abs(ship.imag))


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
