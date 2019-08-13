# merge sort


def msort(lst):
    """Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
    Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.

    """

    print(f"l start {lst}")
    if len(lst) < 2:
        return lst
    result = []
    mid = len(lst)//2
    a = msort(lst[:mid])
    print(f"a {a}")
    b = msort(lst[mid:])
    print(f"b {b}")
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    print(f"res,a,b {result},{a},{b}")
    result.extend(a[i:]+b[j:])
    print(f"res f {result}")
    return result


if __name__ == '__main__':
    print(msort([6, 5, 7, 8, 1, 0, 3, 2]))
