#!/usr/bin/env python3

from math import comb


_HAND_SIZE = 7
_DECK_SIZE = 67
_WIN_CONS = 12
_LANDS = 25
_ROCKS = 11
_OTHER_CARDS = 19


def _compute(_deck_size, _win_cons, _lands, _rocks, _other_cards):
    assert _deck_size - _win_cons - _lands - _rocks - _other_cards == 0
    winning_hands_with_narco = 0
    winning_hands_no_narco = 0
    total_hands = comb(_deck_size, _HAND_SIZE)
    for lands in (2, _HAND_SIZE):
        for rocks in range(1, _HAND_SIZE):
            for win_cons in range(1, _HAND_SIZE):
                other_cards = _HAND_SIZE - lands - rocks - win_cons
                if other_cards >= 0:
                    hands = 1
                    hands *= comb(_lands, lands)
                    hands *= comb(_rocks, rocks)
                    hands *= comb(_win_cons, win_cons)
                    hands_with_narco = hands * comb(_other_cards, other_cards)
                    winning_hands_with_narco += hands_with_narco
                    hands_no_narco = hands * comb(_other_cards - 1, other_cards)
                    winning_hands_no_narco += hands_no_narco
    probability_with_narco = round(winning_hands_with_narco * 100 / total_hands, 2)
    probability_no_narco = round(winning_hands_no_narco * 100 / total_hands, 2)
    print("The probabilities of a good starting hand are:")
    print(f"  - with Narcomoeba in hand:    {probability_with_narco}%")
    print(f"  - without Narcomoeba in hand: {probability_no_narco}%")
    print("")


if __name__ == "__main__":
    print("### Stock 67 (no Belcher)")
    _compute(_DECK_SIZE, _WIN_CONS, _LANDS, _ROCKS, _OTHER_CARDS)

    # print("### Stock 67 (with Belcher)")
    # _compute(_DECK_SIZE, _WIN_CONS + 1, _LANDS, _ROCKS, _OTHER_CARDS - 1)

    print("### 61 cards (-3 lands, -3 rocks, no Belcher)")
    _compute(_DECK_SIZE - 6, _WIN_CONS, _LANDS - 3, _ROCKS - 3, _OTHER_CARDS)

    # print("### 61 cards (-3 lands, -3 rocks, with Belcher)")
    # _compute(_DECK_SIZE - 6, _WIN_CONS + 1, _LANDS - 3, _ROCKS - 3, _OTHER_CARDS - 1)

    print("### 61 cards (-2 lands, -3 rocks, -1 Informer, no Belcher)")
    _compute(_DECK_SIZE - 6, _WIN_CONS - 1, _LANDS - 2, _ROCKS - 3, _OTHER_CARDS)

    # print("### 61 cards (-2 lands, -3 rocks, -1 Informer, with Belcher)")
    # _compute(_DECK_SIZE - 6, _WIN_CONS, _LANDS - 2, _ROCKS - 3, _OTHER_CARDS - 1)

    print("### 60 cards (-3 lands, -3 rocks, -1 Informer, no Belcher)")
    _compute(_DECK_SIZE - 7, _WIN_CONS - 1, _LANDS - 3, _ROCKS - 3, _OTHER_CARDS)

    # print("### 60 cards (-3 lands, -3 rocks, -1 Informer, with Belcher)")
    # _compute(_DECK_SIZE - 7, _WIN_CONS, _LANDS - 3, _ROCKS - 3, _OTHER_CARDS - 1)

    print("### 60 cards (-2 lands, -4 rocks, -1 Informer, no Belcher)")
    _compute(_DECK_SIZE - 7, _WIN_CONS - 1, _LANDS - 2, _ROCKS - 4, _OTHER_CARDS)

    # print("### 60 cards (-2 lands, -4 rocks, -1 Informer, with Belcher)")
    # _compute(_DECK_SIZE - 7, _WIN_CONS, _LANDS - 2, _ROCKS - 4, _OTHER_CARDS - 1)

    print("### 60 cards (-2 lands, -3 rocks, -2 Informer, no Belcher)")
    _compute(_DECK_SIZE - 7, _WIN_CONS - 2, _LANDS - 2, _ROCKS - 3, _OTHER_CARDS)

    # print("### 60 cards (-2 lands, -3 rocks, -2 Informer, with Belcher)")
    # _compute(_DECK_SIZE - 7, _WIN_CONS - 1, _LANDS - 2, _ROCKS - 3, _OTHER_CARDS - 1)

    print("### 69 cards (+1 land, +1 rock, no Belcher)")
    _compute(_DECK_SIZE + 2, _WIN_CONS, _LANDS + 1, _ROCKS + 1, _OTHER_CARDS)

    # print("### 69 cards (+1 land, +1 rock, with Belcher)")
    # _compute(_DECK_SIZE + 2, _WIN_CONS + 1, _LANDS + 1, _ROCKS + 1, _OTHER_CARDS - 1)
