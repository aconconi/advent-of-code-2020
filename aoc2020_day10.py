"""
    Advent of Code 2020
    Day 10: Adapter Array
"""

from collections import Counter


def read_puzzle_input(file_name):
    """read file as list of integers"""
    puzzle_input = open(file_name, "r").read().splitlines()
    return [int(line) for line in puzzle_input]


def day10_part1(data):
    adapters = sorted(data)
    adapters.append(adapters[-1] + 3)
    diff_count = Counter()
    rating = 0
    for a in adapters:
        diff_count[a - rating] += 1
        rating = a

    return diff_count[1] * diff_count[3]



def day10_part2(data):
    # Sort adapters by joltage and add device's built-in joltage adapter
    adapters = [0] + sorted(data)
    dest = adapters[-1] + 3
    adapters.append(dest)

    # Build a graph representing possible connections between adapters.
    graph = {}
    for i, adapter in enumerate(adapters):
        graph[adapter] = [x for x in adapters[i + 1 :] if x - adapter <= 3]

    # Coveniently enough, the graph is a DAG in topological order,
    # and counting paths from each node to last node is O(V+E).
    pc = Counter()
    pc[dest] = 1
    for adapter in reversed(adapters):
        for neighbour in graph[adapter]:
            pc[adapter] += pc[neighbour]

    # The solution is the number of paths from the first node
    return pc[0]


# Part 1
input_data = read_puzzle_input("data/day10.txt")
print("What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?")

# Part 2
print("What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?")
print(day10_part2(input_data))


# Test cases
def test_day10_part1():
    assert day10_part1([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]) == 35
    assert day10_part1(read_puzzle_input("data/day10_test.txt")) == 220


def test_day10_part2():
    assert day10_part2([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]) == 8
    assert day10_part2(read_puzzle_input("data/day10_test.txt")) == 19208
