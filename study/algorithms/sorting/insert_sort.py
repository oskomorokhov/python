def insert_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr)
    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    assert insert_sort(arr) == sorted(arr)
    print("all done!")
