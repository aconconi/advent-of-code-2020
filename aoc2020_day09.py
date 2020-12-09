"""
    Advent of Code 2020
    Day 09: Encoding Error
"""


from collections import deque


def read_puzzle_input(file_name):
    """read file as list of integers"""
    puzzle_input = open(file_name, "r").read().splitlines()
    return [int(line) for line in puzzle_input]


def day09_part1(data, max_size):
    valid = deque(maxlen=max_size)
    for i, n in enumerate(data):
        if len(valid) == max_size and all(n not in z for z in valid):
            return n
        valid.append(set(x + n for x in data[max(0, i - max_size) : i]))

    # If we get here, no solution exists.
    return None


def day09_part2(data, target):
    low = 0
    z = 0
    for i, n in enumerate(data):
        z += n
        if i < 2:
            continue
        while z > target:
            z -= data[low]
            low += 1
            if z == target:
                return min(data[low : i + 1]) + max(data[low : i + 1])

    # If we get here, no solution exists.
    return None


# Part 1
input_data = read_puzzle_input("data/day09.txt")
print("What is the first number that does not have this property?")
part1_result = day09_part1(input_data, 25)
print(part1_result)  # Correct answer is 393911906

# Part 2
print("What is the encryption weakness in your XMAS-encrypted list of numbers?")
print(day09_part2(input_data, part1_result))  # Correct answer is 59341885


# Test cases
test_data = read_puzzle_input("data/day09_test.txt")


def test_day09_part1():
    assert day09_part1(test_data, 5) == 127


def test_day09_part2():
    assert day09_part2(test_data, 127) == 62
