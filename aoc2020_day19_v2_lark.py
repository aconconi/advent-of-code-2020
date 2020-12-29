"""
    Advent of Code 2020
    Day 19: Monster Messages
"""

from lark import Lark
from lark.exceptions import UnexpectedEOF, UnexpectedInput


def format_rule(line):
    return " ".join(
        "expr" + t if t.isdigit() else t
        for t in line.replace(":", " :").split(" ")
    )


def read_puzzle_input(file_name):
    lines = open(file_name, "r").read().splitlines()
    blank = lines.index("")
    rules = [format_rule(line) for line in lines[:blank]]
    return rules, lines[blank + 1 :]


def day19_part1(rules, message):
    grammar = "\n".join(rules)
    parser = Lark(grammar, start="expr0")
    matching = len(message)

    for line in message:
        try:
            parser.parse(line)
        except (UnexpectedEOF, UnexpectedInput):
            matching -= 1

    return matching


def day19_part2(rules, message):
    rules.remove(format_rule("8: 42"))
    rules.append(format_rule("8: 42 | 42 8"))

    rules.remove(format_rule("11: 42 31"))
    rules.append(format_rule("11: 42 31 | 42 11 31"))

    return day19_part1(rules, message)


if __name__ == "__main__":
    input_rules, input_message = read_puzzle_input("data/day19.txt")

    # Part 1
    print("How many messages completely match rule 0?")
    print(day19_part1(input_rules, input_message))

    # Part 2
    print("After updating rules 8 and 11, how many messages completely match rule 0?")
    print(day19_part2(input_rules, input_message))


# Test cases


def test_day19_part1():
    rules, message = read_puzzle_input("data/day19_test.txt")
    assert day19_part1(rules, message) == 2

    rules, message = read_puzzle_input("data/day19_test2.txt")
    assert day19_part1(rules, message) == 3


def test_day19_part2():
    rules, imessage = read_puzzle_input("data/day19_test2.txt")
    assert day19_part2(rules, imessage) == 12
