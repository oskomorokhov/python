"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
from singly_linked_list import *
import sys
sys.path.append('D:\prg\python\data_structures')

q = SingleList()
q.append(3)
q.append(7)
q.append(8)
q.append(10)

z = SingleList()
z.append(99)
z.append(1)
z.append(8)
z.append(10)


def main(ll1, ll2):

    if len(ll1) < len(ll2):
        source = ll1
        comp = ll2
    else:
        source = ll2
        comp = ll1

    s = set()

    current_node = source.head
    while current_node is not None:
        s.add(current_node.data)
        current_node = current_node.next

    current_node = comp.head
    while current_node is not None:
        if current_node.data in s:
            break
        current_node = current_node.next
    print(current_node.data)
    return current_node.data


if __name__ == "__main__":
    main(q, z)
