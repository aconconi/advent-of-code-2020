"""
    Advent of Code 2020
    Day 20: Jurassic Jigsaw
"""

import math
import re


def transposed(tile):
    return list("".join(row) for row in zip(*tile))


def flipped_h(tile):
    return list("".join(reversed(row)) for row in tile)


def rotations(tile):
    last = tile
    for _ in range(4):
        yield last
        last = flipped_h(transposed(last))


def all_transforms(tile):
    yield from rotations(tile)
    yield from rotations(transposed(tile))


def shrunk(tile):
    return [row[1:-1] for row in tile[1:-1]]


def read_puzze_input(file_name):
    tiles = {}
    for entry in open(file_name).read().split("\n\n"):
        lines = entry.strip().split("\n")
        tile_id = int(re.fullmatch(r"Tile (\d+):", lines[0]).group(1))
        rows = lines[1:]
        tiles[tile_id] = list(all_transforms(rows))
    return tiles


def recursive_solve(tiles, grid, stack, seen):
    if not stack:
        return True

    (r, c) = stack.pop()
    for tile_id in list(tiles):
        if tile_id in seen:
            continue
        seen.add(tile_id)
        tile_group = tiles[tile_id]

        for tile in tile_group:
            if r > 0 and grid[r - 1][c][1][-1] != tile[0]:
                continue

            if c > 0:
                left_edge = [row[0] for row in tile]
                right_edge = [row[-1] for row in grid[r][c - 1][1]]
                if right_edge != left_edge:
                    continue

            grid[r][c] = (tile_id, tile)

            if recursive_solve(tiles, grid, stack, seen):
                return True

        seen.remove(tile_id)

    stack.append((r, c))
    return False


def solution_grid(tiles):
    grid_side = math.isqrt(len(tiles))
    grid = [[0] * grid_side for _ in range(grid_side)]
    stack = list(
        reversed(list((r, c) for c in range(grid_side) for r in range(grid_side)))
    )

    recursive_solve(tiles, grid, stack, set())
    return grid


def day20_part1(tiles):
    grid = solution_grid(tiles)
    return grid[0][0][0] * grid[-1][0][0] * grid[0][-1][0] * grid[-1][-1][0]


def day20_part2(tiles):
    grid_side = math.isqrt(len(tiles))
    grid = solution_grid(tiles)
    board = [[shrunk(tile[1]) for tile in row] for row in grid]
    tile_n = len(board[0][0])

    def get(r, c):
        return board[r // tile_n][c // tile_n][r % tile_n][c % tile_n]

    board = [
        "".join(get(r, c) for c in range(grid_side * tile_n))
        for r in range(grid_side * tile_n)
    ]

    MONSTER = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]

    pattern_width = len(MONSTER[0])
    image_width = len(board[0])

    for image in all_transforms(board):
        pattern = r"(?=("
        pattern += MONSTER[0].replace(" ", ".")
        pattern += "." * (image_width - pattern_width)
        pattern += MONSTER[1].replace(" ", ".")
        pattern += "." * (image_width - pattern_width)
        pattern += MONSTER[2].replace(" ", ".")
        pattern += "))"

        matches = len(re.findall(pattern, "".join(image)))
        if matches:
            return "".join(board).count("#") - "".join(MONSTER).count("#") * matches


if __name__ == "__main__":
    input_tiles = read_puzze_input("data/day20.txt")

    print("What do you get if you multiply together the IDs of the four corner tiles?")
    print(day20_part1(input_tiles))

    print("How many # are not part of a sea monster?")
    print(day20_part2(input_tiles))


def test_day20_part1():
    assert (day20_part1(read_puzze_input("data/day20_test.txt"))) == 20899048083289


def test_day20_part2():
    assert (day20_part2(read_puzze_input("data/day20_test.txt"))) == 273
