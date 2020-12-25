"""
    Advent of Code 2020
    Day 24: Lobby Layout
"""

import re


# We are using axial coordinates for the hex grid:
# https://www.redblobgames.com/grids/hexagons
DELTA = {
    "e": 1 + 0j,
    "se": 0 + 1j,
    "sw": -1 + 1j,
    "w": -1 + 0j,
    "nw": 0 - 1j,
    "ne": 1 - 1j,
}


def read_puzzle_input(file_name):
    return open(file_name, "r").read().splitlines()


def parse_path(path):
    return re.findall(r"(e|se|sw|w|nw|ne)", path)


def destination(path):
    return sum(DELTA[step] for step in path)


def get_black_tiles(instructions):
    black = set()
    for line in instructions:
        path = parse_path(line)
        dest = destination(path)
        if dest in black:
            black.remove(dest)
        else:
            black.add(dest)
    return black


def neighbors(tile):
    return {tile + d for d in DELTA.values()}


def num_black_neighbors(tile, black):
    return len(neighbors(tile) & black)


def day24_part1(data):
    return len(get_black_tiles(data))


def day24_part2(data):
    black = get_black_tiles(data)
    for _ in range(100):
        # Any black tile with zero or more than 2 black tiles
        # immediately adjacent to it is flipped to white.
        new_black = {
            tile for tile in black if num_black_neighbors(tile, black) in (1, 2)
        }

        # Generate white tiles that have at least a black neighbor.
        # Note we only need to consider the fringe, not the infinite floor!
        white = {t for tile in black for t in neighbors(tile) if t not in black}

        # Any white tile with exactly 2 black tiles
        # immediately adjacent to it is flipped to black.
        new_black |= {tile for tile in white if num_black_neighbors(tile, black) == 2}

        black = new_black

    return len(black)


if __name__ == "__main__":
    input_data = read_puzzle_input("data/day24.txt")

    # Part 1
    print("How many tiles are left with the black side up?")
    print(day24_part1(input_data))

    # Part 2
    print("How many tiles will be black after 100 days?")
    print(day24_part2(input_data))


def test_day24_part1():
    assert day24_part1(read_puzzle_input("data/day24_test.txt")) == 10


def test_day24_part2():
    assert day24_part2(read_puzzle_input("data/day24_test.txt")) == 2208
