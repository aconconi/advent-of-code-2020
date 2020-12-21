"""
    Advent of Code 2020
    Day 21: Allergen Assessment
"""

from collections import defaultdict


def read_puzze_input(file_name):
    # fist pass on iinput data to clean up formatting
    data = []
    for line in open(file_name).read().splitlines():
        recipe, allergenes = line.split(" (contains ")
        allergenes = allergenes.replace(")", "").split(", ")
        data.append((recipe, allergenes))

    # may_contain[ingr] is the set of allergens that may be contained by ingredient ingr
    may_contain = defaultdict(set)

    # recipes_with[alg] is the set of recipes that contain the allergen alg
    recipes_with = defaultdict(set)
    recipes = set()

    # build data structures
    for recipe, allergenes in data:
        for ingredient in recipe.split(" "):
            may_contain[ingredient] |= set(allergenes)

        recipes.add(recipe)

        for a in allergenes:
            recipes_with[a].add(recipe)

    return recipes, recipes_with, may_contain


def day21_part1(recipes, recipes_with, may_contain):
    inert = []

    for ingredient, allergenes in may_contain.items():
        for a in allergenes.copy():
            if any(ingredient not in r for r in recipes_with[a]):
                allergenes.remove(a)
        if not allergenes:
            inert.append(ingredient)

    return sum(ingredient in recipe for recipe in recipes for ingredient in inert)


def day21_part2(may_contain):
    dangerous = []
    while True:
        try:
            # get the next ingredient with unique allergene associated
            # and not tracked as dangerous yet
            single_ing, single_alg = next(
                (ingredient, allergenes)
                for ingredient, allergenes in may_contain.items()
                if len(allergenes) == 1 and ingredient not in dangerous
            )

            # if such ingredient exist, add it to list of dangerous ingredients
            # and remove it from candidates of all other ingredients
            dangerous.append(single_ing)
            for ingredient, allergenes in may_contain.items():
                if ingredient != single_ing:
                    allergenes -= single_alg

        except StopIteration:
            # if such ingredient does not exist, we're done!
            return ",".join(sorted(dangerous, key=lambda x: next(iter(may_contain[x]))))


if __name__ == "__main__":
    recipes, recipes_with, may_contain = read_puzze_input("data/day21.txt")

    print("How many times do any of those ingredients appear?")
    print(day21_part1(recipes, recipes_with, may_contain))

    print("What is your canonical dangerous ingredient list?")
    print(day21_part2(may_contain))
