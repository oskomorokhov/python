import json
"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # solution 1 ,recursive repr on arguments
        return '{}(val={!r}, left={!r}, right={!r})'.format(self.__class__.__name__, self.val, self.left, self.right)

    def serialize_1(self) -> str:
        # solution 1 ,recursive repr on arguments, result string is exec/eval-ready
        return repr(self)

    @classmethod
    def deserialize_1(cls, string: str = None) -> object:
        # solution 1, eval string containing the command to re-build the bin tree
        return eval(string, {"__builtins__": None}, {'Node': cls})

    def serialize_2(self, sentiel: str = '#') -> list:
        # solution 2, do a depth-first tree traversal (left branch first), replace missing arcs/children with sentiel object
        # outputs as list, wrap into json.dumps() to get a string
        Tlist = [self.val]
        if self.left is None:
            Tlist.append(sentiel)
        else:
            Tlist.extend(self.left.serialize_2())
        if self.right is None:
            Tlist.append(sentiel)
        else:
            Tlist.extend(self.right.serialize_2())
        return Tlist

    @classmethod
    def deserialize_2(cls, lst: list = None, sentiel: str = '#') -> object:
        # solution 2, traverse through list obtained via json.loads() , recursively call class initialization on adjacent elements (children)
        # if sentiel is encountered, replace arc with None
        def _shift(index):
            if lst[index] == sentiel:
                return None, index+1
            val = lst[index]
            left, index = _shift(index+1)
            right, index = _shift(index)
            return cls(val, left, right), index
        return _shift(0)[0]


if __name__ == "__main__":

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    tree_dump = json.dumps(node.serialize_2())
    tree = Node.deserialize_2(json.loads(tree_dump))
    assert Node.deserialize_2(Node.serialize_2(
        node)).left.left.val == 'left.left'
    print("all tests passed")
