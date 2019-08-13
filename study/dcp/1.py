"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def adder_bf(lst, k):
    # brute force O(n^2)
    # sanity checks here (base, edge, negative, zero+k, duplicates, etc)
    for i, n1 in enumerate(lst[:-1]):
        for n2 in lst[i+1:]:
            print("check", n1, n2)
            if n1+n2 == k:
                print(n1, n2)
                return True
    return


def adder_bs(lst, k):
    # binary search, O(log(n)) plus O(n*log(n)) for pre-sorting the list
    # sanity checks here (base, edge, negative, zero+k, duplicates, etc)
    def b_search(lst, k, num):
        goal = k-num
        print("num is", num, "looking for", goal, "in", lst)
        if len(lst) <= 3:
            for n in range(len(lst)):
                if lst[n] == goal:
                    print(num, "+", lst[n], "=", k)
                    return True
        else:
            mid = len(lst)//2
            if goal == lst[mid]:
                print("GOT MID", num, "+", lst[mid], "=", k)
                return True
            elif goal < lst[mid]:
                return b_search(lst[:mid], k, num)
            else:
                return b_search(lst[mid:], k, num)
        print("complement not found")
        return False

    for num in lst[:-1]:
        s = b_search(lst, k, num)
        if s:
            break
    return s


def adder_pair_scan(lst, k):
    # iterate through list, store complement towards target of each number in hash set (for O(1) lookups)
    # if any number sees itself in set of complements, pair found
    comps = set()

    for num in lst:
        if num in comps:
            print(num, "+", k-num, "=", k)
            return True
        else:
            comps.add(k-num)
    return False


if __name__ == "__main__":
    lst = [8, 4, 2, 4]
    k = 8
    result = adder_pair_scan(lst, 8)
    print(result)
