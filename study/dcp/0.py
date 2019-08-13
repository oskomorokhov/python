"""
Return a new sorted merged list from K sorted lists, each with size N
"""

import heapq


def merge_n_sort_1(lol):
    # BF
    l = []
    for e in lol:
        l.extend(e)
    return sorted(l)


def merge_n_sort_2(lol):

    result = []

    heap = [(l[0], i, 0) for i, l in enumerate(lol) if l]

    heapq.heapify(heap)

    while heap:

        val, lst_index, item_index = heapq.heappop(heap)

        result.append(val)

        if item_index + 1 < len(lol[lst_index]):
            next = (lol[lst_index][item_index+1], lst_index, item_index+1)
            heapq.heappush(heap, next)

    return result


if __name__ == "__main__":
    import timeit
    lst = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
    assert merge_n_sort_1(lst) == [10, 12, 15, 15, 17, 20, 20, 30, 32]
    assert merge_n_sort_2(lst) == [10, 12, 15, 15, 17, 20, 20, 30, 32]
    print("BF", timeit.timeit(
        "assert merge_n_sort_1(lst) == [10, 12, 15, 15, 17, 20, 20, 30, 32]", setup="from __main__ import merge_n_sort_1,lst", number=1000))
    print("HEAP", timeit.timeit(
        "assert merge_n_sort_2(lst) == [10, 12, 15, 15, 17, 20, 20, 30, 32]", setup="from __main__ import merge_n_sort_2,lst", number=1000))

    print("all tests passed")
