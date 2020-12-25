"""
    Advent of Code 2020
    Day 25: Combo Breaker
"""

# INPUT = (door_public_key, card_public_key)
TEST_INPUT = (17807724, 5764801)
PUZZLE_INPUT = (6929599, 2448427)


def find_loop_size(pub_key):
    value = 1
    subject = 7
    loop_size = 0
    while True:
        if value == pub_key:
            return loop_size
        loop_size += 1
        value *= subject
        value %= 20201227


def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject
        value %= 20201227
    return value


def day25_part1(data):
    door_pub, card_pub = data
    door_ls = find_loop_size(door_pub)
    card_ls = find_loop_size(card_pub)
    key1 = transform(door_pub, card_ls)
    key2 = transform(card_pub, door_ls)
    assert key1 == key2
    return key1


if __name__ == "__main__":
    # Part 1 and 2 :-)
    print("What encryption key is the handshake trying to establish?")
    print(day25_part1(PUZZLE_INPUT))


def test_day25_part1():
    assert day25_part1(TEST_INPUT) == 14897079
