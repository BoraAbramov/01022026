
import random

number = random.randint(1, 10)
print(number)

random.seed(42)

float_rnd = random.random()
print(float_rnd)

print(int(10 * random.random()) + 1)

print(random.uniform(5, 10))

print(random.choice([1, "yes", "no", 0]))

print(random.randrange(3, 30 + 3, 3))