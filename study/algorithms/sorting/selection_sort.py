# selection sort


def ssort(lst):
    """ The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, 
    and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. 
    The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), 
    and moving the sublist boundaries one element to the right.

    """

    pivot = 0

    while pivot < len(lst):
        current_min = lst[pivot]
        new_min = None
        for num in lst[pivot+1:]:
            if num < current_min:
                current_min = new_min = num
        if new_min:
            lst[lst.index(new_min)
                ], lst[pivot] = lst[pivot], lst[lst.index(new_min)]
        pivot += 1
    return lst


if __name__ == '__main__':
    print("original list", [3, 44, 38, 5, 47,
                            15, 36, 26, 27, 2, 46, 4, 19, 50, 48])
    print(ssort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))
