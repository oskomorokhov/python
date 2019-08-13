"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def foo(string: str = "", k: int = 0) -> str:

    subs = []
    pivot = 0
    while pivot < len(string)-k:
        for i in range(2, len(string)):
            if len(set(string[pivot:i])) == k:
                subs.append(string[pivot:i])
        pivot += 1
    print(sorted(subs, key=len, reverse=True))
    return max(subs, key=len)


if __name__ == "__main__":
    s = "abcba"
    k = 2
    assert(foo(s, k)) == "bcb"
    s = "abcaaaaaaaaaaaaedfgtttttttttt"
    k = 3
    assert(foo(s, k)) == "bcb"
    print('all tests passed')
