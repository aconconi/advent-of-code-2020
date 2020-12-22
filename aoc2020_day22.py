"""
    Advent of Code 2020
    Day 22: Crab Combat
"""


def read_puzze_input(file_name):
    deck1, deck2 = open(file_name).read().split("\n\n")
    return [
        [int(c) for c in deck1.splitlines()[1:]],
        [int(c) for c in deck2.splitlines()[1:]]
    ]


def deck_score(deck):
    return sum(card * (len(deck) - i) for i, card in enumerate(deck))


def day22_part1(decks):
    winner = None
    while all(deck for deck in decks):
        cards = [deck.pop(0) for deck in decks]
        winner = cards.index(max(cards))
        decks[winner].extend(cards if winner == 0 else reversed(cards))
    return deck_score(decks[winner])


def play_recursive_game(decks):
    seen = set()
    winner = None

    # play as along as both players have cards to draw
    while all(deck for deck in decks):
        # if there was a previous round in this game that had exactly the same cards
        # in the same order in the same players' decks, the game instantly ends
        # in a win for player 0. 
        state = (tuple(decks[0]), tuple(decks[1]))
        if state in seen:
            winner = 0
            break

        # Otherwise, this round's cards must be in a new configuration; the players
        # begin the round by each drawing the top card of their deck as normal.
        seen.add(state)
        cards = [deck.pop(0) for deck in decks]

        # If both players have at least as many cards remaining in their deck
        # as the value of the card they just drew, the winner of the round
        # is determined by playing a new game of Recursive Combat.
        if all(len(deck) >= card for deck, card in zip(decks, cards)):
            # To play a sub-game of Recursive Combat, each player creates
            # a new deck by making a copy of the next cards in their deck
            # (the quantity of cards copied is equal to the number on the
            # card they drew to trigger the sub-game).
            recursive_decks = [list(deck[:card]) for deck, card in zip(decks, cards)]
            winner = play_recursive_game(recursive_decks)
        else:
            winner = cards.index(max(cards))

        decks[winner].extend(cards if winner == 0 else reversed(cards))

    # One of the two players has no cards left;
    # the winner of the last round is the winner of the game.
    return winner


def day22_part2(decks):
    winner = play_recursive_game(decks)
    return deck_score(decks[winner])


if __name__ == "__main__":
    file_name = "data/day22.txt"

    # Part 1
    input_decks = read_puzze_input(file_name)
    print("Part 1: What is the winning player's score?")
    print(day22_part1(input_decks))

    # Part 2
    # must read input again because input_decks was modified in Part 1
    input_decks = read_puzze_input(file_name)
    print("Part 2: What is the winning player's score?")
    print(day22_part2(input_decks))
