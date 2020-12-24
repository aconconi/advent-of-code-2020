"""
    Advent of Code 2020
    Day 23: Crab Cups
"""
import array

TEST_INPUT = "389125467"
PUZZLE_INPUT = "614752839"


def play(labels, cups, moves):
    # Set up a linked list using an array, with nxt[i] = successor of i.
    # The Python array module is more efficient than dict or list for this task.
    nxt = array.array("I", range(1, cups + 2))

    # Link given labels together in a closed cycle.
    for x, after_x in zip(labels, labels[1:] + [labels[0]]):
        nxt[x] = after_x

    # If cups are more then the given labels (i.e. we are in Part 2 of the puzzle)
    # then adjust the successor of the last label and the last cup index
    # to build the correct cycle.
    if cups > len(labels):
        nxt[labels[-1]] = len(labels) + 1
        nxt[cups] = labels[0]

    # At the beginning the current cup is the first label.
    current = labels[0]

    for _ in range(1, moves + 1):
        # The crab picks up the three cups that are immediately clockwise
        # of the current cup.
        pick = [nxt[current], nxt[nxt[current]], nxt[nxt[nxt[current]]]]

        # They are removed from the circle; cup spacing is adjusted as
        # necessary to maintain the circle.
        nxt[current] = nxt[pick[-1]]

        # The crab selects a destination cup: the cup with a label
        # equal to the current cup's label minus one. If this would
        # select one of the cups that was just picked up, the crab will
        # keep subtracting one until it finds a cup that wasn't just
        # picked up. If at any point in this process the value goes below
        # the lowest value on any cup's label, it wraps around to the
        # highest value on any cup's label instead.
        dest = current
        while True:
            dest -= 1
            if dest == 0:
                dest = cups
            if dest not in pick:
                break

        # The crab places the cups it just picked up so that they are
        # immediately clockwise of the destination cup. They keep the
        # same order as when they were picked up.
        after_dest = nxt[dest]
        nxt[dest] = pick[0]
        nxt[pick[-1]] = after_dest

        # The crab selects a new current cup: the cup which is
        # immediately clockwise of the current cup.
        current = nxt[current]

    # Return linked list as result.
    return nxt


def day23_part1(labels):
    cups = len(labels)
    nxt = play(labels, cups, 100)
    solution = ""
    c = 1
    for _ in range(cups - 1):
        c = nxt[c]
        solution += str(c)
    return solution


def day23_part2(labels):
    nxt = play(labels, cups=10 ** 6, moves=10 ** 7)
    return nxt[1] * nxt[nxt[1]]


if __name__ == "__main__":
    data = [int(c) for c in PUZZLE_INPUT]

    # Part 1
    print("What are the labels on the cups after cup 1?")
    print(day23_part1(data))

    # Part 2
    print("What do you get if you multiply their labels together?")
    print(day23_part2(data))


def test_day23_part1():
    assert day23_part1([int(c) for c in TEST_INPUT]) == "67384529"


def test_day23_part2():
    assert day23_part2([int(c) for c in TEST_INPUT]) == 149245887792
