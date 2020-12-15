"""
    Advent of Code 2020
    Day 15: Rambunctious Recitation
"""


def solve(numbers, target):
    seen = [None] * (target + 1)

    for turn, n in enumerate(numbers[:-1], 1):
        seen[n] = turn

    last_spoken = numbers[-1]

    for turn in range(len(numbers) + 1, target + 1):
        if seen[last_spoken]:
            speak = turn - 1 - seen[last_spoken]
        else:
            speak = 0

        seen[last_spoken] = turn - 1
        last_spoken = speak

    return last_spoken


def day15_part1(numbers):
    return solve(numbers, 2020)


def day15_part2(numbers):
    return solve(numbers, 30000000)


if __name__ == "__main__":
    puzzle_input = (11, 0, 1, 10, 5, 19)

    # Part 1
    print("Given your starting numbers, what will be the 2020th number spoken?")
    print(day15_part1(puzzle_input))

    # Part 1
    print("Given your starting numbers, what will be the 30000000th number spoken?")
    print(day15_part2(puzzle_input))


# Test cases
test_cases = [
    ([0, 3, 6], 436, 175594),
    ([1, 3, 2], 1, 2578),
    ([2, 1, 3], 10, 3544142),
    ([1, 2, 3], 27, 261214),
    ([2, 3, 1], 78, 6895259),
    ([3, 2, 1], 438, 18),
    ([3, 1, 2], 1836, 362),
]


def test_day15_part1():
    for tc, expected, _ in test_cases:
        assert day15_part1(tc) == expected


def test_day15_part2():
    for tc, _, expected in test_cases:
        assert day15_part2(tc) == expected
