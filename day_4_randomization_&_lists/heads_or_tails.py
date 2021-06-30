import random

seed = int(input("Create a seed number: "))
random.seed(seed)

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

