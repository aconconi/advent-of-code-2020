"""
    Advent of Code 2020
    Day 19: Monster Messages
"""

import re


def read_puzzle_input(file_name):
    lines = open(file_name, "r").read().splitlines()
    blank = lines.index("")
    rules = dict()
    for line in lines[:blank]:
        i, r = line.split(":")
        r = r.replace('"', "")
        rules[i] = r.strip().split(" ")

    return rules, lines[blank + 1 :]


def build_regex(expr, rules):
    result = []
    for t in expr:
        if t.isdigit():
            s = rules[t]
            if "|" in s:
                result.append("(")
                result.extend(build_regex(s, rules))
                result.append(")")
            else:
                result.extend(build_regex(s, rules))
        else:
            result.append(t)
    return result


def day19_part1(rules, message):
    pattern = re.compile("".join(build_regex(["0"], rules)))
    return sum(pattern.fullmatch(line) is not None for line in message)


def day19_part2(rules, message):
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    rules["8"] = "( 42 )+".split()
    build = [" 42 " * i + " 31 " * i for i in range(1, 5)]
    build = "|".join(build).strip()
    rules["11"] = build.split()
    pattern = re.compile("".join(build_regex(["0"], rules)))
    return sum(pattern.fullmatch(line) is not None for line in message)


if __name__ == "__main__":
    input_rules, input_message = read_puzzle_input("data/day19.txt")

    # Part 1
    print("How many messages completely match rule 0?")
    print(day19_part1(input_rules, input_message))

    # Part 2
    print("After updating rules 8 and 11, how many messages completely match rule 0?")
    print(day19_part2(input_rules, input_message))
