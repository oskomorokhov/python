import random


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right

        self._is_left_evaluated = False
        self._is_right_evaluated = False

    @property
    def left(self):
        if not self._is_left_evaluated:
            if random.random() < 0.5:
                self._left = Node(0)

        self._is_left_evaluated = True
        return self._left

    @property
    def right(self):
        if not self._is_right_evaluated:
            if random.random() < 0.5:
                self._right = Node(0)

        self._is_right_evaluated = True
        return self._right


def generate():
    return Node(0)


if __name__ == "__main__":
    tree = generate()
    tree.left
    tree.right
    print(tree.__dict__)
