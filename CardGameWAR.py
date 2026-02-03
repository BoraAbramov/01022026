
import random

_pscore = 0
_PCscore = 0

while True:
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    suit1 = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card1 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    if _pscore == 10 or _PCscore == 10:
        break
    print("player card:", card, suit, end="\n"); print("PC card:", card1, suit1)
    if card == "J":
        card = 11
    if card == "Q":
        card = 12
    if card == "K":
        card = 13
    if card == "A":
        card = 14
    if card1 == "J":
        card1 = 11
    if card1 == "Q":
        card1 = 12
    if card1 == "K":
        card1 = 13
    if card1 == "A":
        card1 = 14
    while True:
        if card == card1:
            print("draw no points")
            break
        if card > card1:
            print("Player wins the round (+1 point)")
            _pscore += 1
            print("score:", end="\n"); print("player score -", _pscore, end="\n"); print("PC score -", _PCscore, end="\n"); print("------------------------------------")
            break
        else:
            print("PC wins the round (+1 point)")
            _PCscore += 1
            print("score:", end="\n"); print("player score -", _pscore, end="\n"); print("PC score -", _PCscore, end="\n"); print("------------------------------------")
            break