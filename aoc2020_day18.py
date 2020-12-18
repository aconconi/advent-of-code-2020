"""
    Advent of Code 2020
    Day 17: Operation Order
"""


import operator
import re


def read_puzzle_input(file_name):
    return open(file_name, "r").read().splitlines()


def shunting_yard(tokens, ops):
    rpn = []
    stack = []

    for token in tokens:
        if token.isdigit():
            rpn.append(token)
        elif token in ops:
            while stack and stack[-1] in ops and ops[stack[-1]][0] >= ops[token][0]:
                rpn.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            try:
                while stack[-1] != "(":
                    rpn.append(stack.pop())
            except IndexError as MistmatchedParentesis:
                raise Exception("Mismatched parenthesis") from MistmatchedParentesis
            try:
                stack.pop()
            except IndexError as MistmatchedParentesis:
                raise Exception("Mismatched parenthesis") from MistmatchedParentesis
        else:
            raise ValueError("Unknown token: " + token)
    while stack:
        rpn.append(stack.pop())

    return rpn


def eval_rpn(tokens, ops):
    stack = []
    for t in tokens:
        if t.isdigit():
            stack.append(int(t))
        elif t in "+*":
            second = stack.pop()
            first = stack.pop()
            stack.append(ops[t][1](first, second))
        else:
            raise Exception("Unknown token: " + t)
    result = stack.pop()
    return result


def tokenize(s):
    tokenizer = re.compile(r"\s*([()+*/-]|\d+)")
    tokens = []
    current_pos = 0
    while current_pos < len(s):
        match = tokenizer.match(s, current_pos)
        if match is None:
            raise ValueError("Syntax error")
        tokens.append(match.group(1))
        current_pos = match.end()
    return tokens


def evaluate(expression, ops):
    tokens = tokenize(expression)
    rpn = shunting_yard(tokens, ops)
    return eval_rpn(rpn, ops)


def day18_part1(data):
    # Non-standard operators precedence: addition and multiplication have the same precedence.
    ops = {"*": (2, operator.mul), "+": (2, operator.add)}
    return sum(evaluate(line, ops) for line in data)


def day18_part2(data):
    # Non-standard operators precedence: addition is evaluated before multiplication.
    ops = {"*": (2, operator.mul), "+": (3, operator.add)}
    return sum(evaluate(line, ops) for line in data)


if __name__ == "__main__":
    input_data = read_puzzle_input("data/day18.txt")
    print("Evaluate the expression on each line of the homework; what is the sum of the resulting values?")
    print(day18_part1(input_data))  # Correct answer is 21022630974613

    print("What do you get if you add up the results of evaluating the homework problems using these new rules?")
    print(day18_part2(input_data))  # Correct answer is 169899524778212

# Test cases


def test_day18_part1():
    test_data = [
        ("1 + 2 * 3 + 4 * 5 + 6", 71),
        ("2 * 3 + (4 * 5)", 26),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + ( 8 + 6 * 4 ) )", 12240),
        ("( ( 2 + 4 * 9) * ( 6 + 9 * 8 + 6 ) + 6 ) + 2 + 4 * 2", 13632),
    ]

    for tc, expected in test_data:
        assert day18_part1([tc]) == expected


def test_day18_part2():
    test_data = [
        ("1 + 2 * 3 + 4 * 5 + 6", 231),
        ("1 + (2 * 3) + (4 * (5 + 6))", 51),
        ("2 * 3 + (4 * 5)", 46),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + ( 8 + 6 * 4 ) )", 669060),
        ("( ( 2 + 4 * 9) * ( 6 + 9 * 8 + 6 ) + 6 ) + 2 + 4 * 2", 23340),
    ]

    for tc, expected in test_data:
        assert day18_part2([tc]) == expected
