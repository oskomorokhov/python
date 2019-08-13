from counting_sort import counting_sort
from math import log10


def radix_sort(arr: list, base: int = 10) -> list:
    # only for non-negative integers

    max_digits = int(log10(max(arr)))+1
    F = [[] for l in range(base)]

    for p in range(max_digits):
        for num in arr:
            digit = (num // base**p) % base
            F[digit].append(num)
        arr = [d for l in F for d in l]
        F = [[] for l in range(base)]

    return arr


if __name__ == "__main__":
    arr = [345, 2342, 1, 23, 923, 122, 4, 0, 99]
    assert radix_sort(arr) == sorted(arr)
    print("all done!")
