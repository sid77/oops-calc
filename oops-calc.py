#!/usr/bin/env python3

from math import comb


_HAND_SIZE = 7


def _sum_hands(spy_effects, black_mana, dark_ritual, other_mana, deck_size):
    other_cards = deck_size - spy_effects - black_mana - dark_ritual - other_mana
    winning_hands = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                for d in range(1, 5):
                    e = _HAND_SIZE - a - b - c - d
                    if e < 0:
                        # this hand is invalid
                        pass
                    else:
                        hands = 1
                        hands *= comb(spy_effects, a)
                        hands *= comb(black_mana, b)
                        hands *= comb(dark_ritual, c)
                        hands *= comb(other_mana, d)
                        hands *= comb(other_cards, e)
                        winning_hands += hands
    return winning_hands


def _compute(deck_size):
    winning_hands = 0
    total_hands = comb(deck_size, _HAND_SIZE)
    # Lotus Petal
    winning_hands += _sum_hands(
        spy_effects=8, black_mana=4, dark_ritual=4, other_mana=23, deck_size=deck_size
    )
    # Agadeem, the Undercrypt
    winning_hands += _sum_hands(
        spy_effects=8, black_mana=4, dark_ritual=4, other_mana=19, deck_size=deck_size
    )
    # Remove the hands with both Lotus Petal and Agadeem, the Undercrypt since
    # they have been added twice. One card is black_mana and the other is
    # other_mana.
    winning_hands -= _sum_hands(
        spy_effects=8, black_mana=4, dark_ritual=4, other_mana=4, deck_size=deck_size
    )
    probability = winning_hands / total_hands
    print(
        f"The probability of a 4 cards hand in a {deck_size} cards deck is {probability}"
    )


if __name__ == "__main__":
    """See README.md"""
    _compute(61)
    _compute(60)
