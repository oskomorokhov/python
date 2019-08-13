import random

M = 0

for i in range(10000):
    trials = [random.randint(0, 1) for x in range(30)]
    if sum(trials) >= 22:
        M += 1

P = M / 10000

print(P)
