"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_1(lst):
    #
    # with division , O(n)+O(n)
    #
    result = []
    p = 1
    for num in lst:
        p *= num
    for num in lst:
        result.append(p/num)
    return result


def product_2(lst):
    #
    # without division, O(n^2)
    #
    result = []
    for num in lst:
        tmp = lst[:]
        tmp.remove(num)
        p = 1
        for n in tmp:
            p *= n
        result.append(p)
    return result


def product_3(lst):
    #
    # without division
    #
    from functools import reduce
    from operator import mul
    result = []
    p = 1
    for i in range(len(lst[:])):
        tmp = lst[i]
        lst[i] = 1
        result.append(reduce(mul, lst))
        lst[i] = tmp
    print(result)
    return result


if __name__ == "__main__":
    assert product_3([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_3([3, 2, 1]) == [2, 3, 6]
    print("all tests passed")
