"""
    Advent of Code 2020
    Day 01: Report Repair
"""


# read input file into lines
with open("data/day01.dat", "r") as data_file:
    lines = data_file.read().splitlines()

data = [int(x) for x in lines]
data.sort()


def day01_part01(numbers):
    return next(n * (2020 - n) for n in numbers if 2020 - n in numbers)


def day01_part02(numbers):
    return next(
        i * j * (2020 - i - j)
        for i in numbers
        for j in (x for x in numbers if i + x < 2020)
        if 2020 - i - j in numbers
    )


# Part 1
print("Find the two entries that sum to 2020; what do you get if you multiply them together?")
print(day01_part01(data))  # Correct answer is 1007104

# Part 2
print("In your expense report, what is the product of the three entries that sum to 2020?")
print(day01_part02(data))  # Correct answer is 18847752


# class Test(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(514579, day01_part01([1721, 979, 366, 299, 675, 1456]))
#     def test_2(self):
#         self.assertEqual(241861950, day01_part02([1721, 979, 366, 299, 675, 1456]))

def test_day01_part1():
    assert day01_part01([1721, 979, 366, 299, 675, 1456]) == 514579
def test_day01_part2():
    assert day01_part02([1721, 979, 366, 299, 675, 1456]) == 241861950
