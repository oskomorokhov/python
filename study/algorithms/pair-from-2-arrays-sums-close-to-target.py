def solution(arr1: list, arr2: list, target: int) -> tuple:

    # all-zeros in both arrays

    if arr1 == arr2 and set(arr1) == {0}:
        return None

    # equivalent arrays
        if arr1 == arr2:
            pass

    s = set(arr1)

    def helper(s: set, arr: list, target: int):
        for num in arr:
            if (target - num) in s:
                return (target-num, num)

    # check if there is a pair that sums to target
    # if not, increase/decrease target by 1

    for inc in range(0, target):
        t1 = target+inc
        a1 = helper(s, arr2, t1)
        if a1:
            return a1
        t2 = target-inc
        a2 = helper(s, arr2, t2)
        if a2:
            return a2


if __name__ == "__main__":
    arr1 = [-1, 3, 8, 2, 9, 5]
    arr2 = [4, 1, 2, 10, 5, 20]
    target = 24

    print(solution(arr1, arr2, target))
