"""
    Advent of Code 2020
    Day 16: Ticket Translation
"""

import re
from math import prod


def read_puzzle_input(file_name):
    pattern_rule = re.compile(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)")
    tickets = []
    rules = []
    # functs = dict()

    for line in open(file_name, "r").read().splitlines():
        if re.match(r"^\d", line):
            # line is a ticket entry (because it starts with a digit)
            tickets.append([int(x) for x in line.split(",")])
        elif (m := pattern_rule.match(line)) :
            # line is a rule, let's parse the rule
            rule = tuple(int(g) if g.isdigit() else g for g in m.groups())
            rules.append(rule)

            # f_name, p1, p2, p3, p4 = rule
            # functs[f_name] = lambda x, a=p1, b=p2, c=p3, d=p4: a <= x <= b or c <= x <= d

    return tickets, rules



def validate_field(rule, field):
    """returns True if the field is accepted by validation rule"""
    _, a, b, c, d = rule
    return a <= field <= b or c <= field <= d


def scan_error(ticket, rules):
    return sum(
        field
        for field in ticket
        if not any(validate_field(rule, field) for rule in rules)
    )


def validate_ticket(rules, ticket):
    """returns True if for each field in the ticket there is at least a rule that accepts that field"""
    return all(
        any(validate_field(rule, field) for rule in rules)
        for field in ticket
    )


def day16_part1(tickets, rules):
    nearby = tickets[1:]
    return sum(scan_error(ticket, rules) for ticket in nearby)


def day16_part2(tickets, rules):
    myticket = tickets[0]
    valid_tickets = [ticket for ticket in tickets if validate_ticket(rules, ticket)]

    # create map of compatible rules for each field index f
    field_ruleset = dict()
    for f in range(len(myticket)):
        field_ruleset[f] = {
            rule[0]
            for rule in rules
            if all(validate_field(rule, ticket[f]) for ticket in valid_tickets)
        }

    # find solution by iteratively assigning rules to field indexes that have only 1 compatible rule
    # and removing the assigned rule from all other indexes
    solution = dict()
    while field_ruleset:
        i, ruleset = next(
            (i, ruleset) for i, ruleset in field_ruleset.items() if len(ruleset) == 1
        )
        single = next(iter(field_ruleset[i]))
        solution[i] = single
        del field_ruleset[i]
        for ruleset in field_ruleset.values():
            ruleset.discard(single)

    # order is now a bijective correspondance between field indexes and rules
    return prod(
        myticket[i]
        for i, rule in solution.items()
        if rule.startswith("departure")
    )


if __name__ == "__main__":
    input_data = read_puzzle_input("data/day16.txt")

    # Part 1
    print("What is your ticket scanning error rate?")
    print(day16_part1(*input_data))

    # Part 2
    print("What do you get if you multiply those six values together?")
    print(day16_part2(*input_data))
