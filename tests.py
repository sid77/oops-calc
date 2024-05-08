import oops_calc

# Test 1
print("# Test 1:")
print("8 cards deck, 4x Spy, 2x Agadeem's, 1x Petal, 1x Ritual")
oops_calc._HAND_SIZE = 7
oops_calc._DECK_SIZE = 8
oops_calc._SPY_EFFECTS = 4
oops_calc._LOTUS_PETALS = 1
oops_calc._DARK_RITUALS = 1
oops_calc._OTHER_MANA = 2
oops_calc._OTHER_CARDS = 0
oops_calc._AGADEEMS = 0
oops_calc._TURNTIMBERS = 2
found = oops_calc._compute(
    oops_calc._DECK_SIZE, oops_calc._OTHER_MANA, oops_calc._OTHER_CARDS
)
expected = 0.75
print(f"expected: {expected}")
print(f"found: {found}")
print("")
assert expected == found

# Test 2
print("# Test 2:")
print("8 cards deck, 4x Spy, 2x Agadeem's, 1x SSG, 1x Ritual")
oops_calc._HAND_SIZE = 7
oops_calc._DECK_SIZE = 8
oops_calc._SPY_EFFECTS = 4
oops_calc._LOTUS_PETALS = 0
oops_calc._DARK_RITUALS = 1
oops_calc._OTHER_MANA = 3
oops_calc._OTHER_CARDS = 0
oops_calc._AGADEEMS = 2
oops_calc._TURNTIMBERS = 0
found = oops_calc._compute(
    oops_calc._DECK_SIZE, oops_calc._OTHER_MANA, oops_calc._OTHER_CARDS
)
expected = 0.75
print(f"expected: {expected}")
print(f"found: {found}")
print("")
assert expected == found

# Test 3
print("# Test 3:")
print("8 cards deck, 4x Spy, 2x Agadeem's, 1x Turntimber, 1x Ritual")
oops_calc._HAND_SIZE = 7
oops_calc._DECK_SIZE = 8
oops_calc._SPY_EFFECTS = 4
oops_calc._LOTUS_PETALS = 0
oops_calc._DARK_RITUALS = 1
oops_calc._OTHER_MANA = 3
oops_calc._OTHER_CARDS = 0
oops_calc._AGADEEMS = 2
oops_calc._TURNTIMBERS = 1
found = oops_calc._compute(
    oops_calc._DECK_SIZE, oops_calc._OTHER_MANA, oops_calc._OTHER_CARDS
)
expected = 0.0
print(f"expected: {expected}")
print(f"found: {found}")
print("")
assert expected == found

# Test 4
print("# Test 4:")
print("8 cards deck, 4x Spy, 3x Petal, 1x Ritual")
oops_calc._HAND_SIZE = 7
oops_calc._DECK_SIZE = 8
oops_calc._SPY_EFFECTS = 4
oops_calc._LOTUS_PETALS = 3
oops_calc._DARK_RITUALS = 1
oops_calc._OTHER_MANA = 0
oops_calc._OTHER_CARDS = 0
oops_calc._AGADEEMS = 0
oops_calc._TURNTIMBERS = 0
found = oops_calc._compute(
    oops_calc._DECK_SIZE, oops_calc._OTHER_MANA, oops_calc._OTHER_CARDS
)
expected = 0.875
print(f"expected: {expected}")
print(f"found: {found}")
print("")
assert expected == found
