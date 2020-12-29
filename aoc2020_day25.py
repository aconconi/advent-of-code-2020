"""
    Advent of Code 2020
    Day 25: Combo Breaker
"""

SUBJECT = 7
DIVIDER = 20201227


def read_puzzle_input(file_name):
    with open(file_name, "r") as data_file:
        return tuple(map(int, data_file.read().splitlines()))


def find_loop_size(pub_key):
    value = 1
    loop_size = 0
    while value != pub_key:
        loop_size += 1
        value = (value * SUBJECT) % DIVIDER
    return loop_size


def transform(subject, loop_size):
    return pow(subject, loop_size, DIVIDER)


def day25_part1(data):
    door_pub, card_pub = data
    door_ls, card_ls = find_loop_size(door_pub), find_loop_size(card_pub)
    key1, key2 = transform(door_pub, card_ls), transform(card_pub, door_ls)
    assert key1 == key2
    return key1


if __name__ == "__main__":
    # Part 1 and 2 :-)
    input_data = read_puzzle_input("data/day25.txt")
    print("What encryption key is the handshake trying to establish?")
    print(day25_part1(input_data))


def test_day25_part1():
    test_case = (17807724, 5764801)
    assert day25_part1(test_case) == 14897079
