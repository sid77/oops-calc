#!/usr/bin/env python3

from scipy.special import comb


_HAND_SIZE = 7


def _comb(N, k):
    return comb(N, k, exact=True, repetition=False)


def _sum_hands(spy_effects, black_mana, dark_ritual, other_mana, other_cards):
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
                        hands *= _comb(spy_effects, a)
                        hands *= _comb(black_mana, b)
                        hands *= _comb(dark_ritual, c)
                        hands *= _comb(other_mana, d)
                        hands *= _comb(other_cards, e)
                        winning_hands += hands
    return winning_hands


def _compute(deck_size):
    winning_hands = 0
    total_hands = _comb(deck_size, _HAND_SIZE)
    # Lotus Petal
    spy_effects = 8
    black_mana = 4
    dark_ritual = 4
    other_mana = 23
    other_cards = deck_size - spy_effects - black_mana - dark_ritual - other_mana
    winning_hands += _sum_hands(
        spy_effects, black_mana, dark_ritual, other_mana, other_cards
    )
    # Agadeem, the Undercrypt
    other_mana = 15
    other_cards = deck_size - spy_effects - black_mana - dark_ritual - other_mana
    winning_hands += _sum_hands(
        spy_effects, black_mana, dark_ritual, other_mana, other_cards
    )
    probability = winning_hands / total_hands
    print(
        f"The probability of a 4 cards hand in a {deck_size} cards deck is {probability}"
    )


if __name__ == "__main__":
    """See README.md"""
    _compute(61)
    _compute(60)
