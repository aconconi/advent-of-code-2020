"""
    Advent of Code 2020
    Day 13: Shuttle Search
"""

import math


def read_puzzle_input(file_name):
    puzzle_input = open(file_name, "r").read().splitlines()
    return (int(puzzle_input[0]), puzzle_input[1].split(","))


def day13_part1(earliest, buses):
    buses = [int(entry) for entry in buses if entry != "x"]
    wait = math.inf
    take = None
    for bus in buses:
        z = bus * math.ceil(earliest / bus) - earliest
        if z < wait:
            wait = z
            take = bus
    return wait * take


def chinese_remainder(numbers, reminders):
    total = 0
    prod = math.prod(numbers)
    for n, a in zip(numbers, reminders):
        pr = prod // n
        total += a * pow(pr, -1, n) * pr
    return total % prod


def day13_part2(buses):
    numbers = [int(bus) for bus in buses if bus != "x"]
    reminders = [int(bus) - i for i, bus in enumerate(buses) if bus != "x"]
    return chinese_remainder(numbers, reminders)


if __name__ == "__main__":
    # Part 1
    timestamp, entries = read_puzzle_input("data/day13.txt")
    print(
        "What is the ID of the earliest bus you can take to the airport\
        multiplied by the number of minutes you'll need to wait for that bus?"
    )
    print(day13_part1(timestamp, entries))  # Correct answer is 161

    # Part 2
    print(
        "What is the earliest timestamp such that all of the listed\
        bus IDs depart at offsets matching their positions in the list?"
    )
    print(day13_part2(entries))  # Correct answer is 213890632230818


# Test cases
def test_day11_part1():
    assert day13_part1(*read_puzzle_input("data/day13_test.txt")) == 295


def test_day11_part2():
    test_cases_part2 = [
        ("7,13,x,x,59,x,31,19", 1068781),
        ("17,x,13,19", 3417),
        ("67,7,59,61", 754018),
        ("67,x,7,59,61", 779210),
        ("67,7,x,59,61", 1261476),
        ("1789,37,47,1889", 1202161486),
    ]

    for tc, expected in test_cases_part2:
        assert day13_part2(tc.split(",")) == expected
