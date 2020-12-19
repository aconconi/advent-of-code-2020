"""
    Advent of Code 2020
    Day 17: Conway Cubes
"""


from itertools import product, repeat


def read_puzzle_input(file_name):
    active = set()
    lines = open(file_name, "r").read().splitlines()
    for row, line in enumerate(lines):
        for column, char in enumerate(line):
            if char == "#":
                active.add((row, column, 0))
    return active


def neighbors(pos):
    for delta in product((-1, 0, +1), repeat=len(pos)):
        if any (d for d in delta):
            yield tuple(p + d for (p, d) in zip(pos, delta))


def bounding_box(nodes):
    box = (range(min(axis) - 1, max(axis) + 2) for axis in zip(*nodes))
    yield from product(*box)


def solve(active):
    for _ in range(6):
        new_active = set()
        for pos in bounding_box(active):
            score = len(active & set(neighbors(pos)))
            if pos in active and score in (2, 3):
                new_active.add(pos)
            else:
                if score == 3:
                    new_active.add(pos)

        active = new_active

    return len(active)



def day17_part1(active):
    return solve(active)


def day17_part2(active):
    active_4d = set(a + (0,) for a in active)
    # print(active_4d)
    return solve(active_4d)


if __name__ == "__main__":
    active = read_puzzle_input("data/day17.txt")

    # Part 1
    print("Part 1: How many cubes are left in the active state after the sixth cycle?")
    print(day17_part1(active))

    # Part 2
    print("Part 2: How many cubes are left in the active state after the sixth cycle?")
    print(day17_part2(active))

