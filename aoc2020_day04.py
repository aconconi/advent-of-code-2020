"""
    Advent of Code 2020
    Day 04: Passport Processing
"""


import re


# pare input so that each line is a passport entry
with open("data/day04.txt", "r") as data_file:
    input_data = [line.replace('\n', ' ') for line in data_file.read().split("\n\n")]


def day04_part1(data):
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return sum(all(field in passport_str for field in required) for passport_str in data)


REQUIRED = {
    "byr": re.compile(r"^(19[2-9][0-9]|200[0-2])$"),
    "iyr": re.compile(r"^20(1[0-9]|20)$"),
    "eyr": re.compile(r"^20(2[0-9]|30)$"),
    "hgt": re.compile(r"^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$"),
    "hcl": re.compile(r"^#[0-9a-f]{6}$"),
    "ecl": re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
    "pid": re.compile(r"^[0-9]{9}$")
}


def is_valid(passport_str: str) -> bool:
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    passport = {value.split(":")[0]: value.split(":")[1] for value in passport_str.split()}

    return all(
        bool(REQUIRED[field].match(passport.get(field, ""))) for field in REQUIRED
    )


def day04_part2(data):
    return sum(is_valid(passport) for passport in data)


# Part 1
print("In your batch file, how many passports are valid?")
print(day04_part1(input_data))  # Correct solution is 192

# Part 2
print("In your batch file, how many passports are valid?")
print(day04_part2(input_data))  # Correct solution is 101


# Test cases
def test_aoc2020_part1():
    part1_testcase = {
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
        "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
        "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
    }
    assert day04_part1(part1_testcase) == 2


def test_aoc2020_part2_all_valid():
    part2_valid = [
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
        "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ]
    assert all(is_valid(p) for p in part2_valid)


def test_aoc2020_part2_all_invalid():
    part2_invalid = [
        "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
        "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007",
    ]
    assert all(not is_valid(p) for p in part2_invalid)
