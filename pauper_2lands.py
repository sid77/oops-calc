#!/usr/bin/env python3

from math import comb


_HAND_SIZE = 7
_DECK_SIZE = 60
_SPY_EFFECTS = 5
_FORESTS = 1
_TAP_LANDS = 1
_LAND_GRANTS = 4
_LAND_CYCLERS = 6
_FAST_MANAS = 8


def compute(
    hand_size=_HAND_SIZE,
    deck_size=_DECK_SIZE,
    spy_effects=_SPY_EFFECTS,
    forests=_FORESTS,
    tap_lands=_TAP_LANDS,
    land_grants=_LAND_GRANTS,
    land_cyclers=_LAND_CYCLERS,
    fast_manas=_FAST_MANAS,
):
    total_hands = comb(deck_size, hand_size)
    good_hands = 0
    # Scenario 1: 1+ spy effects and 2+ between any combination of lands or Land
    # Grants
    #
    # Land Grants are functionally equivalent to a land: a player can either
    # play land and then Land Grant for the missing one or Land Grant, play land
    # and then Land Grant again
    lands = forests + tap_lands + land_grants
    other_cards_in_deck = deck_size - spy_effects - lands
    for spy_effect in range(1, spy_effects):
        for land in range(2, lands):
            other_cards = hand_size - spy_effect - land
            if other_cards >= 0:
                hands = 1
                hands *= comb(spy_effects, spy_effect)
                hands *= comb(lands, land)
                hands *= comb(other_cards_in_deck, other_cards)
                good_hands += hands

    # Scenario 2: 1+ spy effects, exactly 1 Forest and 1+ land cycler
    #
    # As before, Forest and Land Grant are functionally equivalent. We must make
    # sure tap land or other Land Grant are not drawn otherwise we end up in an
    # already analyzed scenario
    lands = forests + land_grants
    other_cards_in_deck = deck_size - spy_effects - lands - land_cyclers - tap_lands
    for spy_effect in range(1, spy_effects):
        for land_cyler in range(1, land_cyclers):
            other_cards = (
                hand_size - spy_effect - 1 - land_cyler
            )  # 1: land or Land Grant in hand
            if other_cards >= 0:
                hands = 1
                hands *= comb(spy_effects, spy_effect)
                hands *= lands  # comb(lands, 1) = lands
                hands *= comb(land_cyclers, land_cyler)
                hands *= comb(other_cards_in_deck, other_cards)
                good_hands += hands

    # Scenario 3: 1+ spy effect, exactly 1 tap land, 1+ fast mana, 1+ land
    # cycler
    #
    # With tap land in hand, we need fast mana and a land cycler to get the
    # missing Forest. We must make sure Forest and Land Grant are not drawn
    # otherwise we end up in an already analyzed scenario
    other_cards_in_deck = (
        deck_size
        - spy_effects
        - tap_lands
        - fast_manas
        - land_cyclers
        - forests
        - land_grants
    )
    for spy_effect in range(1, spy_effects):
        for fast_mana in range(1, fast_manas):
            for land_cyler in range(1, land_cyclers):
                other_cards = (
                    hand_size - spy_effect - 1 - fast_mana - land_cyler
                )  # 1: tap land in hand
                if other_cards >= 0:
                    hands = 1
                    hands *= comb(spy_effects, spy_effect)
                    # hands *= 1 # comb(1,1) = 1 (tap land)
                    hands *= comb(fast_manas, fast_mana)
                    hands *= comb(land_cyclers, land_cyler)
                    hands *= comb(other_cards_in_deck, other_cards)
                    good_hands += hands

    # Scenario 4: 1+ spy effect, 2+ fast mana, 2+ land cycler
    #
    # We must make sure no lands nor Land Grant is in hand otherwise we end up
    # in an already analyzed scenario
    other_cards_in_deck = (
        deck_size
        - spy_effects
        - fast_manas
        - land_cyclers
        - forests
        - tap_lands
        - land_grants
    )
    for spy_effect in range(1, spy_effects):
        for fast_mana in range(2, fast_manas):
            for land_cyler in range(2, land_cyclers):
                other_cards = hand_size - spy_effect - fast_mana - land_cyler
                if other_cards >= 0:
                    hands = 1
                    hands *= comb(spy_effects, spy_effect)
                    hands *= comb(fast_manas, fast_mana)
                    hands *= comb(land_cyclers, land_cyler)
                    hands *= comb(other_cards_in_deck, other_cards)
                    good_hands += hands

    probability = round(good_hands * 100 / total_hands, 2)
    print(
        f"The probabilities of a good starting hand with {spy_effects} spy effects is: {probability}%"  # noqa: E501
    )


if __name__ == "__main__":
    compute(spy_effects=4)
    compute(spy_effects=5)
    compute(spy_effects=6)
