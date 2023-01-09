# oops-calc
Oops, all spells! Hands calculator

## DISCLAIMER
I have no idea of what I am doing. Last time I looked into probabilities was a LONG time ago so take these values with a pinch of salt.

From dusting off my knowledge on the subject, it seems to me [this StackExchange answer](https://boardgames.stackexchange.com/questions/23212/whats-the-probability-of-having-a-combo-on-the-first-turn-in-mtg) makes sense so I implemented it. If this assumption is not true, well, everything coded here is a giant load of bullshit 🙂. There might be implementation errors as well.

## Objective
This script computes the probaility of a "T1 kill on a mull to 4" hand to understand why this deck mulligans so well. And also because the constraints for this hand make the computation much easier.

## Magic Numbers
The reference deck is a stock 61 cards Oops with Reanimate.

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
 - Remove 2 Chrome Mox, they require a second card to be imprinted on them to be used so they do not fit in the 4 cards hand as well.
 - Add 4 Summoner's Pact, they can tutor Elvish Spirit Guide and fit into the 4 cards hand constraints.

The total is 30 - 1 - 2 + 4 = 31.

### Others
Everything else: 61 - 31 - 8 = 22.

## The hand
The hand we are looking for is a 4 cards T1 kill which is constructed in the following way:
 - 1 Spy effect
 - 1 Black mana source
 - 1 Dark Ritual
 - 1 Mana of any type
 - 3 other cards

There are only 2 cards that can directly provide the initial Black mana: Lotus Petal or Agadeem, the Undercrypt. There are 4 copies of each in the deck.

### Lotus Petal
Opening a Lotus Petal is the easiest way to build the target hand. The number of winning hands is:

f(Lotus Petal) * f(Dark Ritual) * f(Spy effect) * f(one other mana) * f(other three cards)

All of those functions are Binomial with the following parameters:
 - f(Spy effects) has parameters N=8 and k=1
 - f(Lotus Petal) has parameters N=4 and k=1
 - f(Dark Ritual) has parameters N=4 and k=1
 - f(one other mana) has parameters N=31-4-4=23 and k=1
 - f(other three cards) has parameters N=22 and k=3

and all of their permutations (i.e. two Spy effects and so on).

### Agadeem, the Undercrypt
Game rules state that only one Land card can be played each turn. A 4 cards hand based on Agadeem, the Undercrypt can not play Turntimber, Serpentine Wood as additional mana source so this card goes into the Others pool.

Additionally, I have to exclude Lotus Petal since it has already been included in the section above. I took a shortcut here and moved this card in the Others pool as well but I think I ended up counting some hands twice nevertheless.

Maybe the correct approach is to still count it as Other Mana and then remove the hands with both Spy effect, Lotus Petal, Agadeem, the Undercrypt, Dark Ritual and other cards.

So, to recap:
 - f(Spy effects) has parameters N=8 and k=1
 - f(Agadeem, the Undercrypt) has parameters N=4 and k=1
 - f(Dark Ritual) has parameters N=4 and k=1
 - f(one other mana) has parameters N=31-4-4-4-4=15 and k=1
 - f(other three cards) has parameters N=22+4+4=30 and k=3

and all of their permutations (i.e. two Spy effects and so on).

## Results
If I didn't make any stupid mistakes, the probability of a T1 kill on a mull to 4 is 12.96%.
