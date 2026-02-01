
import random
from random import choice

_rock = 1
_papper = 2
_sciccors = 3

while True:
    player = int(input("please enter your choice: 1 - rock, 2 - paper, 3 - sciccors: "))
    pc = random.choice([1, 2, 3])
    if player == pc:
        print("Draw!")
    if player == 1 and pc == 3 or player == 2 and pc == 1 or player == 3 and pc == 2:
        print("You win!")
    if player == 1 and pc == 2 or player == 2 and pc == 3 or player == 3 and pc == 1:
        print("PC win!")

