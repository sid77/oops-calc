#!/usr/bin/env python3

from math import comb


_HAND_SIZE = 7
_DECK_SIZE = 61
# see README.md for these magic numbers
_SPY_EFFECTS = 8
_LOTUS_PETALS = 4
_DARK_RITUALS = 4
_OTHER_MANA = 24
_OTHER_CARDS = 21
_AGADEEMS = 4
_TURNTIMBERS = 4


def _compute(deck_size, other_mana, other_cards):
    winning_hands = 0
    total_hands = comb(deck_size, _HAND_SIZE)
    # Lotus Petal
    assert (
        _LOTUS_PETALS + _DARK_RITUALS + _SPY_EFFECTS + other_mana + other_cards
        == deck_size
    )
    for lotus_petals in range(1, _LOTUS_PETALS + 1):
        for dark_rituals in range(1, _DARK_RITUALS + 1):
            for spy_effects in range(1, _SPY_EFFECTS + 1):
                remaining_cards = _HAND_SIZE - lotus_petals - dark_rituals - spy_effects
                for extra_mana in range(0, remaining_cards + 1):
                    fillers = remaining_cards - extra_mana
                    if lotus_petals == 1 and dark_rituals == 1 and extra_mana == 0:
                        # this hand doesn't work
                        continue
                    if fillers >= 0:
                        hands = 1
                        hands *= comb(_LOTUS_PETALS, lotus_petals)
                        hands *= comb(_DARK_RITUALS, dark_rituals)
                        hands *= comb(_SPY_EFFECTS, spy_effects)
                        hands *= comb(other_mana, extra_mana)
                        hands *= comb(other_cards, fillers)
                        winning_hands += hands
    # Agadeem, the Undercrypt
    adjusted_other_mana = other_mana - _AGADEEMS - _TURNTIMBERS
    adjusted_other_cards = other_cards + _TURNTIMBERS
    assert (
        _LOTUS_PETALS
        + _AGADEEMS
        + _DARK_RITUALS
        + _SPY_EFFECTS
        + adjusted_other_mana
        + adjusted_other_cards
        == deck_size
    )
    for agadeems in range(1, _AGADEEMS + 1):
        for dark_rituals in range(1, _DARK_RITUALS + 1):
            for spy_effects in range(1, _SPY_EFFECTS + 1):
                remaining_cards = _HAND_SIZE - agadeems - dark_rituals - spy_effects
                for extra_mana in range(0, remaining_cards + 1):
                    fillers = remaining_cards - extra_mana
                    if dark_rituals == 1 and extra_mana == 0:
                        # this hand doesn't work
                        continue
                    if fillers >= 0:
                        hands = 1
                        hands *= comb(_LOTUS_PETALS, 0)
                        hands *= comb(_AGADEEMS, agadeems)
                        hands *= comb(_DARK_RITUALS, dark_rituals)
                        hands *= comb(_SPY_EFFECTS, spy_effects)
                        hands *= comb(adjusted_other_mana, extra_mana)
                        hands *= comb(adjusted_other_cards, fillers)
                        winning_hands += hands
    probability = winning_hands / total_hands
    return probability


if __name__ == "__main__":
    print("### Stock 61")
    probability = _compute(_DECK_SIZE, _OTHER_MANA, _OTHER_CARDS)
    print(f"The probability of a 4 cards winning hand is {probability}")
    print("")

    print("### Stock 60, usually -1x Cabal ritual")
    probability = _compute(_DECK_SIZE - 1, _OTHER_MANA - 1, _OTHER_CARDS)
    print(f"The probability of a 4 cards winning hand is {probability}")
    print("")

    print("### Stock 61 on Lively Dirge, usually -1x Cabal ritual +1x Lively Dirge")
    probability = _compute(_DECK_SIZE, _OTHER_MANA - 1, _OTHER_CARDS + 1)
    print(f"The probability of a 4 cards winning hand is {probability}")
    print("")

    print("### Stock 60 on Lively Dirge, usually -2x Cabal ritual +1x Lively Dirge")
    probability = _compute(_DECK_SIZE - 1, _OTHER_MANA - 2, _OTHER_CARDS + 1)
    print(f"The probability of a 4 cards winning hand is {probability}")
    print("")
