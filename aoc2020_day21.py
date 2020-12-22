"""
    Advent of Code 2020
    Day 21: Allergen Assessment
"""

from collections import Counter


def read_puzze_input(file_name):
    possible = {}
    ingredient_counter = Counter()

    with open(file_name) as input_file:
        for line in input_file:
            recipe, allergens = line.split(" (contains ")
            ingredients = set(recipe.split())
            allergens = allergens[:-2].split(", ")

            for i in ingredients:
                ingredient_counter[i] += 1

            for allergene in allergens:
                if allergene in possible:
                    possible[allergene] &= ingredients
                else:
                    possible[allergene] = ingredients.copy()

    return possible, ingredient_counter


def get_dangerous(possible):
    dangerous = {}
    while possible:
        # get the next allergen associated with excatly one ingredient
        single_allergen = next(
            allergen
            for allergen, ingredients in possible.items()
            if len(ingredients) == 1
        )

        # get the ingredient associated with that allergen, and remove it from the dictionary
        # note we are popping a set from a (dict) by key (single_allergen),
        # then we are popping an element from that set
        single_ingredient = possible.pop(single_allergen).pop()

        # single_ingredient cannot be associated with any other allergen
        for ingredients in possible.values():
            ingredients.discard(single_ingredient)

        # track dangerous ingredient
        dangerous[single_allergen] = single_ingredient

    return dangerous


def day21_part1(dangerous, ingredient_counter):
    return sum(
        c for i, c in ingredient_counter.items() if i not in dangerous.values()
    )


def day21_part2(dangerous):
    return ",".join(
        ing for _, ing in sorted(dangerous.items())
    )


if __name__ == "__main__":
    possible, ingredient_counter = read_puzze_input("data/day21.txt")
    dangerous = get_dangerous(possible)

    # Part 1
    print("How many times do any of those ingredients appear?")
    print(day21_part1(dangerous, ingredient_counter))

    # Part 2
    print("What is your canonical dangerous ingredient list?")
    print(day21_part2(dangerous))