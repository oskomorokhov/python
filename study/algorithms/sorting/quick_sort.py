# quick sort


def qsort(lst):
    """ Pick an element, called a pivot, from the array.
    Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
    Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.

    """

    # list is sorted if there's only 1 element
    if len(lst) < 2:
        return lst
    # set first element as pivot. can also select random pos
    pivot = lst[0]
    # store_index is index of next item after pivot
    store_index = lst.index(pivot)+1
    # iterate on items from pivot to the end, if item is less than pivot swap items at store index and at i, incr. store_index
    for i in range(lst.index(pivot)+1, len(lst)):
        if lst[i] < pivot:
            lst[store_index], lst[i] = lst[i], lst[store_index]
            store_index += 1
    # swap items at pivot and store_index-1 positions, pivot is now on its sorted pos
    lst[lst.index(pivot)], lst[store_index -
                               1] = lst[store_index-1], lst[lst.index(pivot)]
    # partition the list in before & after pivot chunks
    a, b = lst[:lst.index(pivot)], lst[lst.index(pivot)+1:]
    # recursively run qsort on chunks, concatenate their results and insert pivot in between
    lst = qsort(a)+[pivot]+qsort(b)
    return lst


if __name__ == '__main__':
    print([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48])
    print(qsort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))
