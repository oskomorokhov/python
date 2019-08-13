"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def staircase_bin(steps: int = 0, opts: list = [], root=None) -> list:

    if not steps or not opts or len(opts) != 2:
        return None

    root = Node(steps)

    while steps > 0:

        if steps-opts[0] >= 0:
            root.left = Node(opts[0])

        if steps-opts[1] >= 0:
            root.right = Node(opts[1])

        root = root.left
        steps = steps-opts[0]

    print(root)


def staircase(steps: int = 0, opts: list = [], prefix: list = [], ways: list = []) -> list:

    if not steps or not opts:
        if prefix not in ways:
            ways.append(prefix)
        return None

    for opt in opts:
        if steps-opt >= 0:
            staircase(steps-opt, opts, prefix+[opt], ways)

    return ways


if __name__ == "__main__":
    N = 4
    k = [1, 2]
    result = staircase_bin(N, k)

    N = 4
    k = [1, 2, 3]
    result = staircase(N, k)
    print("all tests passed")
