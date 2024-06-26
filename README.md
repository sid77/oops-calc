# oops-calc
Oops, all spells! Hands calculator

## DISCLAIMER
I have no idea of what I am doing. Last time I looked into probabilities was a LONG time ago so take these values with a pinch of salt.

From dusting off my knowledge on the subject, it seems to me [this StackExchange answer](https://boardgames.stackexchange.com/questions/23212/whats-the-probability-of-having-a-combo-on-the-first-turn-in-mtg) makes sense so I implemented it. If this assumption is not true, well, everything coded here is a giant load of bullshit 🙂. There might be implementation errors as well.

## Changelog
2024/06029 - Add calculator for good opening hands in Modern Oops, All Spells!. This 67 cards deck is taken from the [Modern Oops, All Spells! Primer](https://solitairethegathering.net/index.php?title=Oops:Primer), a "good" starting hand is one with at least 2x lands, 1x mana rock and 1x win condition. The "no Belcher" comment means I don't count Goblin Charblecher as a win condition in these opening hands

2024/05/02 - Update stock deck list with 1x Chrome Mox, 4x Cabal Ritual split. Fix fillers count in Agadeem, the Undercrypt hands

2023/01/11 - Force k=0 for Lotus Petal in Agadeem, the Undercrypt hands

2023/01/09 - Initial release

## Objective
This script computes the probaility of a "T1 win on a mull to 4" hand to understand why this deck mulligans so well. And also because the constraints for this hand make the computation much easier.

## Magic Numbers
The [reference deck](Oops.txt) is a stock 61 cards Oops with Reanimate.

There are three different pools of cards in a reference Oops deck:
 - Spy effects, these cards dump your library into the graveyard.
 - Mana cards, these cards are used to add either 1 or more mana of different colors to your pool.
 - Others, these cards execute the combo or protect it.

### Spy effects
This is the easy one, there are 8 cards in total.

### Mana cards
This is where things get complicated, fast.

The number of cards that reads "add mana" is 30. From this total:
 - Remove 1 Wild Cantor, this is a mana fixer that can not be used in a 4 cards hand.
 - Remove 1 Chrome Mox, it requires a second card to be imprinted on them to be used so it does not fit in the 4 cards hand as well.
 - Add 4 Summoner's Pact, they can tutor Elvish Spirit Guide and fit into the 4 cards hand constraints.

The total is 30 - 1 - 1 + 4 = 32.

### Others
Everything else: 61 - 32 - 8 = 21.

## The hand
The hand we are looking for is a 4 cards T1 win which is constructed in the following way:
 - 1 Spy effect
 - 1 Black mana source
 - 1 Dark Ritual
 - 1 Mana of any type
 - 3 other cards

There are only 2 cards that can directly provide the initial Black mana: Lotus Petal or Agadeem, the Undercrypt. There are 4 copies of each in the deck.

### Lotus Petal
Opening a Lotus Petal is the easiest way to build the target hand. The number of winning hands is:

f(Lotus Petal) * f(Dark Ritual) * f(Spy effect) * f(one other mana) * f(other three cards)

A card from Other Mana is needed if and only if we open exactly 1 Lotus Petal and exactly 1 Dark Ritual. If we open 2+ of any of those cards we threat the rest of the deck as fillers for the initial hand.

All of those functions are Binomial with the following parameters:
 - f(Spy effects) has parameters N=8 and k>=1
 - f(Lotus Petal) has parameters N=4 and k>=1
 - f(Dark Ritual) has parameters N=4 and k>=1
 - f(one other mana) has parameters N=32-4-4=24 and k>=1
 - f(other three cards) has parameters N=21 and k<=3 if we need one other mana otherwise has parameters N=61-4-4-8=45 and k<=3

### Agadeem, the Undercrypt
Game rules state that only one Land card can be played each turn. A 4 cards hand based on Agadeem, the Undercrypt can not play Turntimber, Serpentine Wood as additional mana source so this card goes into the Others pool.

It also can not play more than one Agadeem, the Undercrypt if there are multiple copies in it but it can play 2+ Dark Ritual, with the same considerations as above.

Additionally, I have to exclude Lotus Petal since it has already been included in the section above.

So, to recap:
 - f(Lotus Petal) has parameters N=4 and k=0
 - f(Spy effects) has parameters N=8 and k>=1
 - f(Agadeem, the Undercrypt) has parameters N=4 and k>=1
 - f(Dark Ritual) has parameters N=4 and k>=1
 - f(one other mana) has parameters N=32-4-4-4-4=16 and k>=1
 - f(other three cards) has parameters N=21+4=25 and k<=3 if we need one other mana otherwise has parameters N=61-4-4-4-8=41 and k<=3

## Results
If I didn't make any stupid mistakes, the probability of a T1 win on a mull to 4 is 12.16%.
