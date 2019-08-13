"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival(tree, count=0):

    if tree:
        print(f"we are at {tree.val}")
    else:
        return 0

    print("check left and right")
    if tree.left is None and tree.right is None:
        print("leaf, +1")
        return 1

    left = count_unival(tree.left, count)
    print("count after left", left)
    right = count_unival(tree.right, count)
    print("count after right", right)

    count += left+right
    print("count l+r", count)

    if tree.left and tree.val != tree.left.val:
        print(f"{tree.val} != {tree.left.val}")
        print("count", count)
        return count
    if tree.right and tree.val != tree.right.val:
        print(f"{tree.val} != {tree.right.val}")
        print("count", count)
        return count

    count += 1
    return count


if __name__ == "__main__":

    node1 = Node('0', Node('1'), Node('0'))
    node1.right.left = Node('1')
    node1.right.right = Node('0')
    node1.right.left.left = Node('1')
    node1.right.left.right = Node('1')

    r1 = count_unival(node1)
    print("result1", r1)

    node2 = Node('5', Node('1'), Node('5'))
    node2.left.left = Node('5')
    node2.left.right = Node('5')
    node2.right.right = Node('5')

    r2 = count_unival(node2)
    print("result2", r2)

    node3 = Node('5', Node('4'), Node('5'))
    node3.left.left = Node('4')
    node3.left.right = Node('4')
    node3.right.right = Node('5')

    r3 = count_unival(node3)
    print("result2", r3)

    assert(count_unival(node1)) == 5
    assert(count_unival(node2)) == 4
    assert(count_unival(node3)) == 5

    print("all tests passed")
