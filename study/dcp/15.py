"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random


def probe(array: list = []) -> int:
    random_element = None
    for i, e in enumerate(array):
        if i == 0:
            random_element = e
        elif random.randint(1, i+1) == 1:
            random_element = e
    return random_element


if __name__ == "__main__":
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(probe(stream))
