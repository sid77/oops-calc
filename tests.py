import oops_calc

# Test 1
print("Test 1: 8 cards deck, 4x spy, 2x Agadeem's, 1x Petal, 1x Ritual")
oops_calc._HAND_SIZE = 7
oops_calc._DECK_SIZE = 8
oops_calc._SPY_EFFECTS = 4
oops_calc._LOTUS_PETALS = 1
oops_calc._DARK_RITUALS = 1
oops_calc._OTHER_MANA = 2
oops_calc._OTHER_CARDS = 0
oops_calc._AGADEEMS = 0
oops_calc._TURNTIMBERS = 2
probability = oops_calc._compute(
    oops_calc._DECK_SIZE, oops_calc._OTHER_MANA, oops_calc._OTHER_CARDS
)
print(f"The probability of a 4 cards winning hand is {probability}")
assert probability == 0.75
