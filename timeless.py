#!/usr/bin/env python3

from math import comb


_HAND_SIZE = 7
_DECK_SIZE = 60
_SPY_EFFECTS = 4
_ELENDAS = 4
_LANDS = 12
_DARK_RITUALS = 4
_SORINS = 4
_MOXEN = 4
_REANIMATES = 4
_TSEIZES = 2


def compute(
    hand_size=_HAND_SIZE,
    deck_size=_DECK_SIZE,
    spy_effects=_SPY_EFFECTS,
    elendas=_ELENDAS,
    lands=_LANDS,
    dark_rituals=_DARK_RITUALS,
    sorins=_SORINS,
):
    total_hands = comb(deck_size, hand_size)
    good_hands = 0
    # Scenario 1: 1+ untap land, 2+ Dark Rituals, 1+ Spy, no Sorins
    other_cards_in_deck = deck_size - lands - dark_rituals - spy_effects - sorins
    for land in range(1, lands):
        for dark_ritual in range(2, dark_rituals):
            for spy_effect in range(1, spy_effects):
                other_cards = hand_size - land - dark_ritual - spy_effect
                if other_cards >= 0:
                    hands = 1
                    hands *= comb(lands, land)
                    hands *= comb(dark_rituals, dark_ritual)
                    hands *= comb(spy_effects, spy_effect)
                    hands *= comb(other_cards_in_deck, other_cards)
                    good_hands += hands

    # Scenario 2: 1+ untap land, 1+ Dark Ritual, 1+ Sorin, 1+ Spy or Elenda
    other_cards_in_deck = (
        deck_size - lands - dark_rituals - sorins - spy_effects - elendas
    )
    action_cards = spy_effects + elendas
    for land in range(1, lands):
        for dark_ritual in range(1, dark_rituals):
            for sorin in range(1, sorins):
                for action_card in range(1, action_cards):
                    other_cards = hand_size - land - dark_ritual - sorin - action_card
                    if other_cards >= 0:
                        hands = 1
                        hands *= comb(lands, land)
                        hands *= comb(dark_rituals, dark_ritual)
                        hands *= comb(sorins, sorin)
                        hands *= comb(action_cards, action_card)
                        hands *= comb(other_cards_in_deck, other_cards)
                        good_hands += hands

    probability = round(good_hands * 100 / total_hands, 2)
    print(f"The probability of a 4 cards winning hand is {probability}%")


if __name__ == "__main__":
    print("# 60 cards deck:")
    compute()
    print("# 61 cards deck:")
    compute(deck_size=61)
