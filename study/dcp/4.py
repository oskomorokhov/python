"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
You can modify the input array in-place.
"""


def find_pos_int(array: list = None) -> int:
    # sort and check if next element is prev element + 1
    # solution is O(n) but sort is O(n*log(n))
    #
    array = sorted(array)
    print(array)
    if array[-1] <= 0:
        return 1
    for i, num in enumerate(array[:-1]):
        if num > 0:
            if num+1 == array[i+1]:
                continue
            else:
                print(num+1)
                return num+1
    else:
        print(array[-1]+1)
        return array[-1]+1


def find_pos_int_2(array: list = None) -> int:
    # start with min/max set to 1. For each element that is >=2, check if its -1 and +1 numbers are in array and compare to current min/max. Update min/max based on lookup results.
    # O(n) for iteration and O(n) for each lookup
    min_int = max_int = 1
    for i, num in enumerate(array):
        if num >= 2:
            if num-1 not in array:
                if num-1 >= min_int and min_int in array:
                    min_int = num - 1
                    print("min", min_int)
            elif num+1 not in array:
                if num+1 >= min_int and min_int in array:
                    min_int = num + 1
                    print("min", min_int)
            elif num > max_int:
                max_int = num
                print("max", max_int)

    return max_int+1 if min_int in array else min_int


if __name__ == "__main__":
    assert find_pos_int_2([3, 4, -1, 1]) == 2
    assert find_pos_int_2([1, 2, 0]) == 3
    assert find_pos_int_2([-3, -2, -1]) == 1
    assert find_pos_int_2([1, 2, 3, 6, 7, 8, 9]) == 4
    assert find_pos_int_2([1, 2, 3, 4, 5, 6, 7]) == 8
    print("all tests passed")
