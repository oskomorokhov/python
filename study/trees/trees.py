# Binary trees, heaps, traversal, sorting, etc
#


class Node(object):
    """Class used to construct Nodes & Binary Trees
    same as in binarytree module
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#tree = Node(1, Node(2, Node(4), Node(7)), Node(3, Node(5), Node(6)))


# Inorder travertal of bin tree (LEFT,ROOT,RIGHT), outputs result as list
def Tinorder(tree, Tlist=[]):
    if tree:
        Tinorder(tree.left)
        Tlist.append(tree.value)
        Tinorder(tree.right, Tlist)
    return Tlist

# Construct the BST by attaching "values" to "nodes", key in each node > any key in left sub-tree and <= any key in right sub-tree


def Tinsert(node, value):
    if node is None:
        print("INSERT: inserting", value, "node")
        node = Node(value)
    else:
        if value < node.value:
            print("INSERT: this child is less than its parent, recur LEFT",
                  value, "<", node.value)
            node.left = Tinsert(node.left, value)
        if value >= node.value:
            print("INSERT: this child is greater than its parent, recur RIGHT",
                  value, ">", node.value)
            node.right = Tinsert(node.right, value)
    return node

# Given an array, builds a BST and then performs inorder traversal to perform a sort


def TTreeSort(array):
    root = None
    print(
        "SORT: need to constuct new BST first, passing empty node & 0-index of given array to INSERT", array[0])
    root = Tinsert(root, array[0])
    print("SORT: our BST now has the root which is", root)
    for i in range(1, len(array)):
        print("SORT: passing next node", array[i], "to INSERT into tree")
        bst = Tinsert(root, array[i])
    srt = Tinorder(bst)
    return srt


arr = [5, 4, 7, 2, 11, 14, 6]
print(arr)
print(TTreeSort(arr))
