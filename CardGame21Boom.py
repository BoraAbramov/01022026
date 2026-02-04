
import random

_p1 = 0
_p2 = 0
_stop_start = None

while True:
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    if _p1 == 21:
        print("Player 1 starts with total: ", _p1)
    if _p1 > 21:
        print("❌ Player 1 is disqualified")
        break
    _stop_start = int(input(print("Choose:\n 0 = STOP\n 1 = CONTINUE")))
    if _stop_start == 0:
        print("player 1 cards: ", card, suit, end="\n")
        print("Total: ", "0", end="\n\n")
        break
    if _stop_start == 1:
        print("player 1 cards: ", card, suit, end="\n")
        if card == "J" or card == "Q" or card == "K":
            card = 10
        if card == "A":
            card = 1
        _p1 += card
        print("Total: ", _p1, end="\n\n")
        continue
while True:
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    if _p2 == 21:
        print("Player 2 starts with total: ", _p1)
    if _p2 > 21:
        print("❌ Player 2 is disqualified")
        break
    _stop_start = int(input(print("Choose:\n 0 = STOP\n 1 = CONTINUE")))
    if _stop_start == 0:
        print("player 2 cards: ", card, suit, end="\n")
        print("Total: ", "0", end="\n\n")
        break
    if _stop_start == 1:
        print("player 1 cards: ", card, suit, end="\n")
        if card == "J" or card == "Q" or card == "K":
            card = 10
        if card == "A":
            card = 1
        _p2 += card
        print("Total: ", _p2, end="\n\n")
        continue
if _p1 > _p2:
    print("Player 1 starts with total: ", _p1)
