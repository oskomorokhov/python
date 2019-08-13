from math import log10


def counting_sort(lst: list) -> list:
    # only for non-negative integers
    base = 10**(int(log10(max(lst)))+1)
    F = [0] * base
    for num in lst:
        F[num] += 1
    lst = []
    for i in range(len(F)):
        if F[i]:
            lst.extend([i]*F[i])
    return lst


if __name__ == '__main__':
    arr = [3, 4, 8, 5, 4, 1, 2, 3, 123, 2, 0, 4456, 7, 6, 0, 99, 3]
    assert counting_sort(arr) == sorted(arr)
    print("all done!")
