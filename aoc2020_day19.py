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
        rules[i]  = r.replace('"', "").strip()

    return rules, lines[blank + 1 :]


def build_regex(expr, rules):
    result = ""
    for t in expr.split(' '):
        if t.isdigit():
            s = rules[t]
            par_left, par_right = ("(", ")") if "|" in s else ("", "")
            result += par_left + build_regex(s, rules) + par_right
        else:
            result += t
    return result


def day19_part1(rules, message):
    pattern = re.compile("".join(build_regex("0", rules)))
    return sum(pattern.fullmatch(line) is not None for line in message)


def day19_part2(rules, message):
    # Rule 8: 42 | 42 8
    rules["8"] = "( 42 ) +"
    # Rule 11: 42 31 | 42 11 31
    rules["11"] = "|".join([" 42 " * i + " 31 " * i for i in range(1, 5)]).strip()
    return day19_part1(rules, message)



if __name__ == "__main__":
    input_rules, input_message = read_puzzle_input("data/day19.txt")

    # Part 1
    print("How many messages completely match rule 0?")
    print(day19_part1(input_rules, input_message))

    # Part 2
    print("After updating rules 8 and 11, how many messages completely match rule 0?")
    print(day19_part2(input_rules, input_message))


