"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

from operator import itemgetter, attrgetter


def rgb1(lst: list) -> list:

    def foo(string: str) -> int:
        if string == 'R':
            result = 0
        elif string == 'G':
            result = 1
        else:
            result = 2
        return result

    return sorted(lst, key=foo)


def rgb2(lst: list) -> list:

    indexes = [[] for x in range(3)]
    for i in range(len(lst)):
        if lst[i] == 'R':
            indexes[0].append(i)
        elif lst[i] == 'G':
            indexes[1].append(i)
        else:
            indexes[2].append(i)

    return [lst[i] for x in indexes for i in x]


def rgb3(a: list) -> list:

    lo = 0
    hi = len(lst) - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 'R':
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 'G':
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return lst


if __name__ == "__main__":
    lst = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    assert rgb1(lst) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
    assert rgb2(lst) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
    assert rgb3(lst) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
    print('all done')
