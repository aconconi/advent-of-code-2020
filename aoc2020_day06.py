"""
    Advent of Code 2020
    Day 06: Custom Customs
"""


# parse an input file that contains multi-line entries
# separated by blank lines into a list of lists
def parse_input(file_name):
    data = [[]]
    with open(file_name, "r") as data_file:
        for line in data_file.read().splitlines():
            if line:
                data[-1].append(line)
            else:
                data.append([])
    return data if data[0] else []


def day06_part1(data):
    return sum(len(set("".join(answers_group))) for answers_group in data)


def day06_part2(data):
    return sum(
        len(set.intersection(*(set(answer) for answer in answers_group)))
        for answers_group in data
    )


# Part 1
input_data = parse_input("data/day06.txt")
print("Part 1: What is the sum of those counts?")
print(day06_part1(input_data))  # Correct answer is 6775

# Part 2
print("Part 2: What is the sum of those counts?")
print(day06_part2(input_data))  # Correct answer is 3356


# Test cases
def test_day06_part1():
    assert day06_part1(parse_input("data/day06_test.txt")) == 11


def test_day06_part2():
    assert day06_part2(parse_input("data/day06_test.txt")) == 6
