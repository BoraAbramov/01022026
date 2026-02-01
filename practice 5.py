
import random

#roll a dice and print the number (1-6) using randint
number = random.randint(1, 6)
print(number)

#generate a random number between 20-200 using randint
number = random.randint(20, 200)
print(number)

#generate 8 numbers between 10 and 20 using sample
print(random.sample(range(10, 20), 8))

#generate a random amount of numbers (between 1-4) of multiples of 3 between 12-48
print(random.sample(range(12, 48 + 3, 3), random.randint(1, 4)))

#choose a random color between "red" "green" "blue" "orange" "white"
print(random.choice(["red", "blue", "orange", "white"]))

#input 3 numbers from the user , then choose randomly 1 of the numbers
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter another number: "))

print(random.choice([x, y, z]))

#choose a random temperature between 35.0-37.5 using uniform
print((random.uniform(35.0, 37.5)))