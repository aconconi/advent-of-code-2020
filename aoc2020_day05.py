"""
    Advent of Code 2020
    Day 05: Binary Boarding
"""


def decode_bp(boarding_pass: str) -> int:
    row = sum(pow(2, 6 - i) if c == "B" else 0 for i, c in enumerate(boarding_pass[:7]))
    col = sum(pow(2, 2 - i) if c == "R" else 0 for i, c in enumerate(boarding_pass[7:]))
    return row * 8 + col


def day05_part1(data):
    return max(decode_bp(boarding_pass) for boarding_pass in data)


def day05_part2(data):
    seats = [decode_bp(boarding_pass) for boarding_pass in data]
    return next(i for i in range(min(seats), max(seats) + 1) if i not in seats)


# Read input lines
with open("data/day05.dat", "r") as data_file:
    lines = data_file.read().splitlines()

# Part 1
print("What is the highest seat ID on a boarding pass?")
print(day05_part1(lines))

# Part 2
print("What is the ID of your seat?")
print(day05_part2(lines))


# Test cases:
def test_decode():
    assert decode_bp("FBFBBFFRLR") == 357  # FBFBBFFRLR: row 44, column 5, seat ID 357.
    assert decode_bp("BFFFBBFRRR") == 567  # BFFFBBFRRR: row 70, column 7, seat ID 567.
    assert decode_bp("FFFBBBFRRR") == 119  # FFFBBBFRRR: row 14, column 7, seat ID 119.
    assert decode_bp("BBFFBBFRLL") == 820  # BBFFBBFRLL: row 102, column 4, seat ID 820
