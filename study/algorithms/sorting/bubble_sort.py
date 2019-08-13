# bubble sort


def bsort(lst):
    """Starting from the beginning of the list, compare every adjacent pair, swap their position if they are not in the right order (the latter one is smaller than the former one). 
    After each iteration, one less element (the last one) is needed to be compared until there are no more elements left to be compared.

    """

    swapped = True
    j = len(lst)
    while swapped and j >= 0:
        swapped = False
        for i in range(j-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        j -= 1
    return(lst)


if __name__ == '__main__':
    print(bsort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))
