
import random

_lucky = random.randint(1, 100)

while True:
    for i in range(0, 3):
        player = int(input("Enter number between 1 and 100: "))
        while player < 0 or player > 100:
                player = int(input("Enter number between 1 and 100 or you die: "))
        if player == _lucky:
            print("Bingo!")
            break
        if i < 2:
            if player > _lucky:
                print("guess lower!")
            else:
                print("guess higher!")
    print("you loose, the lucky number is " + str(_lucky))
    break



