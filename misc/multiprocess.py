import timeit
from multiprocessing import Pool

import math


def f(x): return math.factorial(x)


start = timeit.default_timer()

for x in range(0, 1000):
    print(f(x))

end = timeit.default_timer()

worktimes = (end-start)

start = timeit.default_timer()

with Pool(5) as p:
    print(p.map(f, list(range(0, 1000))))

end = timeit.default_timer()

worktimem = (end-start)

print("one thread", worktimes)
print("multiprocessing", worktimem)
