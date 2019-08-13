"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def largest_sum_1(lst):
    # BF
    sum1 = sum([x for x in lst[::2]])
    sum2 = sum([x for x in lst[1::2]])

    return sum1 if sum1 > sum2 else sum2


def largest_sum_2(lst):
    # one loop
    i = 0
    sum1 = sum2 = 0

    while i < len(lst):
        sum1 += lst[i]
        if i <= len(lst)-2:
            sum2 += lst[i+1]
        i += 2
    print(sum1, sum2)
    return sum1 if sum1 > sum2 else sum2


if __name__ == "__main__":
    lst = [2, 4, 6, 2, 5]
    assert(largest_sum_1(lst)) == 13
    assert(largest_sum_2(lst)) == 13
    print("all test passed")
