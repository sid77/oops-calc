#!/usr/bin/env python3

from math import comb


_HAND_SIZE = 7
_DECK_SIZE = 61
# see README.md for these magic numbers
_SPY_EFFECTS = 8
_LOTUS_PETALS = 4
_DARK_RITUALS = 4
_OTHER_MANA = 23
_OTHER_CARDS = 22
_AGADEEMS = 4
_TURNTIMBERS = 4


def _compute(deck_size=_DECK_SIZE, other_cards=_OTHER_CARDS):
    winning_hands = 0
    total_hands = comb(deck_size, _HAND_SIZE)
    # Lotus Petal
    assert (
        _LOTUS_PETALS + _DARK_RITUALS + _SPY_EFFECTS + _OTHER_MANA + other_cards
        == deck_size
    )
    rest_of_deck = deck_size - _LOTUS_PETALS - _DARK_RITUALS - _SPY_EFFECTS
    # lol
    # assert _LOTUS_PETALS + _DARK_RITUALS + _SPY_EFFECTS + rest_of_deck == deck_size
    for lotus_petals in range(1, 5):
        for dark_rituals in range(1, 5):
            for spy_effects in range(1, 5):
                if lotus_petals == 1 and dark_rituals == 1:
                    # need extra mana
                    for other_mana in range(1, 5):
                        fillers = (
                            _HAND_SIZE
                            - lotus_petals
                            - dark_rituals
                            - spy_effects
                            - other_mana
                        )
                        if fillers >= 0:
                            hands = 1
                            hands *= comb(_LOTUS_PETALS, lotus_petals)
                            hands *= comb(_DARK_RITUALS, dark_rituals)
                            hands *= comb(_SPY_EFFECTS, spy_effects)
                            hands *= comb(_OTHER_MANA, other_mana)
                            hands *= comb(other_cards, fillers)
                            winning_hands += hands
                else:
                    fillers = _HAND_SIZE - lotus_petals - dark_rituals - spy_effects
                    if fillers >= 0:
                        hands = 1
                        hands *= comb(_LOTUS_PETALS, lotus_petals)
                        hands *= comb(_DARK_RITUALS, dark_rituals)
                        hands *= comb(_SPY_EFFECTS, spy_effects)
                        hands *= comb(rest_of_deck, fillers)
                        winning_hands += hands
    # Agadeem, the Undercrypt
    adjusted_other_mana = _OTHER_MANA - _AGADEEMS - _TURNTIMBERS
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
    rest_of_deck -= _AGADEEMS
    assert (
        _LOTUS_PETALS + _AGADEEMS + _DARK_RITUALS + _SPY_EFFECTS + rest_of_deck
        == deck_size
    )
    for agadeems in range(1, 5):
        for dark_rituals in range(1, 5):
            for spy_effects in range(1, 5):
                if dark_rituals == 1:
                    # need extra mana
                    for other_mana in range(1, 5):
                        fillers = (
                            _HAND_SIZE
                            - agadeems
                            - dark_rituals
                            - spy_effects
                            - other_mana
                        )
                        if fillers >= 0:
                            hands = 1
                            hands *= comb(_LOTUS_PETALS, 0)
                            hands *= comb(_AGADEEMS, agadeems)
                            hands *= comb(_DARK_RITUALS, dark_rituals)
                            hands *= comb(_SPY_EFFECTS, spy_effects)
                            hands *= comb(adjusted_other_mana, other_mana)
                            hands *= comb(adjusted_other_cards, fillers)
                            winning_hands += hands
                else:
                    fillers = (
                        _HAND_SIZE - agadeems - dark_rituals - spy_effects - other_mana
                    )
                    if fillers >= 0:
                        hands = 1
                        hands *= comb(_LOTUS_PETALS, 0)
                        hands *= comb(_AGADEEMS, agadeems)
                        hands *= comb(_DARK_RITUALS, dark_rituals)
                        hands *= comb(_SPY_EFFECTS, spy_effects)
                        hands *= comb(rest_of_deck, fillers)
                        winning_hands += hands
    probability = winning_hands / total_hands
    print(
        f"The probability of a 4 cards hand in a {deck_size} cards deck is {probability}"
    )


if __name__ == "__main__":
    _compute(61, 22)
    _compute(60, 21)
