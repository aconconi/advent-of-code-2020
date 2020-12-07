"""
    Advent of Code 2020
    Day 07: Handy Haversacks
"""


with open("data/day07.txt", "r") as data_file:
    input_data = data_file.read().splitlines()

rules = dict()
rules_quant = dict()

for rule in input_data:
    rule = rule.replace("bags", "")
    rule = rule.replace("bag", "")
    rule = rule.replace(".", "")
    rule = rule.split("contain")
    container = "_".join(rule[0].strip().split(" "))
    right = rule[1].split(",")
    right = [x.strip().split(" ") for x in right]
    right = [(x[1] + "_" + x[2], int(x[0])) if len(x) == 3 else None for x in right]
    right = [x for x in right if x]
    rules[container] = set(contained for contained, _ in right)
    rules_quant[container] = dict(
        zip((contained for contained, _ in right), (quant for _, quant in right))
    )


# Iterative implementation for Part 1
def day06_part1_iterative():
    queue = [container for container in rules if "shiny_gold" in rules[container]]
    solutions = set()
    visited = set()

    while queue:
        color = queue.pop(0)
        if color in visited:
            continue
        visited.add(color)
        solutions |= {color} if rules[color] & (solutions | {"shiny_gold"}) else {}
        queue.extend(container for container in rules if color in rules[container])

    return len(solutions)


# Recursive implementation for Part 1
def day06_part1():
    def solve(solutions):
        new_sols = {color for color in rules_quant if rules[color] & solutions} - solutions
        return solutions | new_sols | (solve(new_sols) if new_sols else set())

    return len(solve({"shiny_gold"})) - 1


# Recursive implementation for Part 2
def day06_part2():
    def solve(color):
        return 1 + sum(
            rules_quant[color][contained] * solve(contained)
            for contained in rules_quant[color]
        )

    return solve("shiny_gold") - 1


# Part 1
print("How many bag colors can eventually contain at least one shiny gold bag?")
print(day06_part1())  # Correct answer is 316

# Part 2
print("How many individual bags are required inside your single shiny gold bag?")
print(day06_part2())  # Correct answer is 11310
