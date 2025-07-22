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


def compute_mull_to_4(
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


def compute_self_tseize(
    hand_size=_HAND_SIZE,
    deck_size=_DECK_SIZE,
    spy_effects=_SPY_EFFECTS,
    elendas=_ELENDAS,
    lands=_LANDS,
    dark_rituals=_DARK_RITUALS,
    sorins=_SORINS,
    moxen=_MOXEN,
    reanimates=_REANIMATES,
    tseizes=_TSEIZES,
):
    # A self TSeize hand is composed of 1+ TSeize, 1+ Reanimate, 1+ Spy or
    # Elenda to bring back and 2 mana.
    #
    # This leaves with 4 cards that must generate at least BB.
    #
    # Generating 3 mana and Sorin is not ok because playing Sorin into win con
    # instead is strictly better
    #
    # Similarly, 4 mana and Spy is not ok as well but 4+ mana and Elenda is ok

    total_hands = comb(deck_size, hand_size)
    good_hands = 0

    action_cards = spy_effects + elendas

    # Exactly 2 mana
    # Scenario 1: land, mox and a black pitch card. No Dark Rituals.
    other_cards_in_deck = (
        deck_size
        - tseizes
        - reanimates
        - spy_effects
        - elendas
        - lands
        - moxen
        - dark_rituals
    )
    # we can't pitch the Wurm here
    pitchables = other_cards_in_deck - 1
    # we can't pitch Elenda so run the hands with spy first
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            for spy_effect in range(1, spy_effects):
                for land in range(1, lands):
                    for mox in range(1, 2):  # more than 2 moxen and we can't pitch
                        other_cards = (
                            hand_size - tseize - reanimate - spy_effect - land - mox
                        )
                        if other_cards >= 0:
                            if (
                                tseize == 1
                                and reanimate == 1
                                and spy_effect == 1
                                and land == 1
                            ):
                                # We need something to pitch and space in hand
                                if other_cards > 0:
                                    hands = 1
                                    hands *= comb(tseizes, tseize)
                                    hands *= comb(reanimates, reanimate)
                                    hands *= comb(spy_effects, spy_effect)
                                    hands *= comb(lands, land)
                                    hands *= comb(moxen, mox)
                                    hands *= comb(pitchables, other_cards)
                                    good_hands += hands
                            else:
                                # We already have a black pitch card, add fillers
                                hands = 1
                                hands *= comb(tseizes, tseize)
                                hands *= comb(reanimates, reanimate)
                                hands *= comb(spy_effects, spy_effect)
                                hands *= comb(lands, land)
                                hands *= comb(moxen, mox)
                                hands *= comb(other_cards_in_deck, other_cards)
                                good_hands += hands
    # same as above but with Elenda now (XXX can't be pitched)
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            for elenda in range(1, elendas):
                for land in range(1, lands):
                    for mox in range(1, 2):  # more than 2 moxen and we can't pitch
                        other_cards = (
                            hand_size - tseize - reanimate - elenda - land - mox
                        )
                        if other_cards >= 0:
                            if tseize == 1 and reanimate == 1 and land == 1:
                                # We need something to pitch and space in hand
                                if other_cards > 0:
                                    hands = 1
                                    hands *= comb(tseizes, tseize)
                                    hands *= comb(reanimates, reanimate)
                                    hands *= comb(elendas, elenda)
                                    hands *= comb(lands, land)
                                    hands *= comb(moxen, mox)
                                    hands *= comb(pitchables, other_cards)
                                    good_hands += hands
                            else:
                                # We already have a black pitch card, add fillers
                                hands = 1
                                hands *= comb(tseizes, tseize)
                                hands *= comb(reanimates, reanimate)
                                hands *= comb(elendas, elenda)
                                hands *= comb(lands, land)
                                hands *= comb(moxen, mox)
                                hands *= comb(other_cards_in_deck, other_cards)
                                good_hands += hands

    # Scenario 2: exactly 2 moxen and 2 black pitch cards. No Lands. No Dark Rituals.
    # again, we can't pitch Elenda so run the hands with spy first
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            for spy_effect in range(1, spy_effects):
                other_cards = hand_size - tseize - reanimate - spy_effect - 2
                if other_cards >= 0:
                    hands = 1
                    hands *= comb(tseizes, tseize)
                    hands *= comb(reanimates, reanimate)
                    hands *= comb(spy_effects, spy_effect)
                    hands *= comb(moxen, 2)
                    hands *= comb(pitchables, other_cards)
                    good_hands += hands
    # one more time for exactly one Elenda in hand otherwise we don't have
    # enough cards to pitch
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            other_cards = hand_size - tseize - reanimate - 1 - 2
            if other_cards >= 0:
                hands = 1
                hands *= comb(tseizes, tseize)
                hands *= comb(reanimates, reanimate)
                hands *= comb(elendas, 1)
                hands *= comb(moxen, 2)
                hands *= comb(pitchables, other_cards)
                good_hands += hands

    # Exactly 3 mana
    # Scenario 3: land, exactly 1 Dark Ritual. No Sorins.
    other_cards_in_deck = (
        deck_size
        - tseizes
        - reanimates
        - spy_effects
        - elendas
        - lands
        - dark_rituals
        - sorins
    )
    action_cards = spy_effects + elendas
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            for action_card in range(1, action_cards):
                for land in range(1, lands):
                    other_cards = (
                        hand_size - tseize - reanimate - action_card - land - 1
                    )
                    if other_cards >= 0:
                        hands = 1
                        hands *= comb(tseizes, tseize)
                        hands *= comb(reanimates, reanimate)
                        hands *= comb(action_cards, action_card)
                        hands *= comb(lands, land)
                        hands *= comb(dark_rituals, 1)
                        hands *= comb(other_cards_in_deck, other_cards)
                        good_hands += hands
    # Scenario 4: mox, no lands, exactly 1 Dark Ritual, one other black pitch
    # card. No Sorins.
    other_cards_in_deck = (
        deck_size
        - tseizes
        - reanimates
        - spy_effects
        - elendas
        - lands
        - moxen
        - dark_rituals
        - sorins
    )
    # no Wurm
    pitchables = other_cards_in_deck - 1
    # Elenda can't be pitched to Mox so let's run Spy first
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            for spy_effect in range(1, spy_effects):
                for mox in range(1, 2):  # more than 2 moxen and we can't pitch
                    other_cards = hand_size - tseize - reanimate - spy_effect - mox - 1
                    if other_cards >= 0:
                        if tseize == 1 and reanimate == 1 and spy_effect == 1:
                            # we need something to pitch and space in hand
                            if other_cards > 0:
                                hands = 1
                                hands *= comb(tseizes, tseize)
                                hands *= comb(reanimates, reanimate)
                                hands *= comb(spy_effects, spy_effect)
                                hands *= comb(moxen, mox)
                                hands *= comb(dark_rituals, 1)
                                hands *= comb(pitchables, other_cards)
                                good_hands += hands
                        else:
                            # we have enough to pitch
                            hands = 1
                            hands *= comb(tseizes, tseize)
                            hands *= comb(reanimates, reanimate)
                            hands *= comb(spy_effects, spy_effect)
                            hands *= comb(moxen, mox)
                            hands *= comb(dark_rituals, 1)
                            hands *= comb(other_cards_in_deck, other_cards)
                            good_hands += hands
    # once again, with feelings. For Elenda.
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            for elenda in range(1, elendas):
                for mox in range(1, 2):  # more than 2 moxen and we can't pitch
                    other_cards = hand_size - tseize - reanimate - elenda - mox - 1
                    if other_cards >= 0:
                        if tseize == 1 and reanimate == 1:
                            # we need something to pitch and space in hand
                            if other_cards > 0:
                                hands = 1
                                hands *= comb(tseizes, tseize)
                                hands *= comb(reanimates, reanimate)
                                hands *= comb(elendas, elenda)
                                hands *= comb(moxen, mox)
                                hands *= comb(dark_rituals, 1)
                                hands *= comb(pitchables, other_cards)
                                good_hands += hands
                        else:
                            # we have enough to pitch
                            hands = 1
                            hands *= comb(tseizes, tseize)
                            hands *= comb(reanimates, reanimate)
                            hands *= comb(elendas, elenda)
                            hands *= comb(moxen, mox)
                            hands *= comb(dark_rituals, 1)
                            hands *= comb(other_cards_in_deck, other_cards)
                            good_hands += hands

    # 4+ mana, no Spy
    # Scenario 5: land, 2 or 3 Dark Rituals. No Spies. No Sorins.
    other_cards_in_deck = (
        deck_size
        - tseizes
        - reanimates
        - spy_effects
        - elendas
        - lands
        - dark_rituals
        - sorins
    )
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            for elenda in range(1, elendas):
                for land in range(1, lands):
                    for dark_ritual in range(2, dark_rituals):
                        other_cards = (
                            hand_size - tseize - reanimate - elenda - land - dark_ritual
                        )
                        if other_cards >= 0:
                            hands = 1
                            hands *= comb(tseizes, tseize)
                            hands *= comb(reanimates, reanimate)
                            hands *= comb(elendas, elenda)
                            hands *= comb(lands, land)
                            hands *= comb(dark_rituals, dark_ritual)
                            hands *= comb(other_cards_in_deck, other_cards)
                            good_hands += hands

    # Scenario 6: exactly 1 mox, 2+ Dark Rituals, eventual black pitch card. No
    # Spies. No Sorins. No lands.
    other_cards_in_deck = (
        deck_size
        - tseizes
        - reanimates
        - spy_effects
        - elendas
        - lands
        - moxen
        - dark_rituals
        - sorins
    )
    # no Wurm
    pitchables = other_cards_in_deck - 1
    for tseize in range(1, tseizes):
        for reanimate in range(1, reanimates):
            for elenda in range(1, elendas):
                for dark_ritual in range(2, dark_rituals):
                    other_cards = (
                        hand_size - tseize - reanimate - elenda - dark_ritual - 1
                    )
                    if other_cards >= 0:
                        hands = 1
                        hands *= comb(tseizes, tseize)
                        hands *= comb(reanimates, reanimate)
                        hands *= comb(elendas, elenda)
                        hands *= comb(moxen, 1)
                        hands *= comb(dark_rituals, dark_ritual)
                        hands *= comb(pitchables, other_cards)
                        good_hands += hands

    probability = round(good_hands * 100 / total_hands, 2)
    print(f"The probability of a self TSeize hand is {probability}%")


if __name__ == "__main__":
    print("# Computing mull to 4 hands:")
    print("## 60 cards deck:")
    compute_mull_to_4()
    print("## 61 cards :")
    compute_mull_to_4(deck_size=61)
    print("## 62 cards :")
    compute_mull_to_4(deck_size=62)
    print("")
    print("# Computing self TSeize hands:")
    print("## 2 TSeize, 60 cards")
    compute_self_tseize()
    print("## 4 TSeize, 60 cards")
    compute_self_tseize(tseizes=4)
    print("## 3 TSeize, 61 cards")
    compute_self_tseize(tseizes=3, deck_size=61)
    print("## 4 TSeize, 62 cards")
    compute_self_tseize(tseizes=4, deck_size=62)
