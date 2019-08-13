def choice_sort(arr: list) -> list:

    current_min = 0
    for i in range(1, len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[current_min]:
                arr[current_min], arr[j] = arr[j], arr[current_min]
        current_min += 1

    print(arr)
    return(arr)


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    assert choice_sort(arr) == sorted(arr)
    print("all done!")
