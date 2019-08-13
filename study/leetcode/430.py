"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        if not head:
            return None

        def helper(head, result=[]):
            result.append(head)
            while head.next or head.child:
                if head.child:
                    helper(head.child, result)
                if head.next:
                    result.append(head.next)
                    head = head.next
                else:
                    break
            return result

        flattened = helper(head)

        for e in range(1, len(flattened)):
            flattened[e].child = None
            flattened[e-1].child = None
            flattened[e-1].next = flattened[e]
            flattened[e].prev = flattened[e-1]
        else:
            flattened[-1].next = None

        return flattened[0]
