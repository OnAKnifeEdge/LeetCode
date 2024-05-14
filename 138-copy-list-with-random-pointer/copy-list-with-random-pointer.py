"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        d = {}
        p = head
        while p:
            d[p] = Node(p.val)
            p = p.next
        p = head
        while p:
            if p.next:
                d[p].next = d[p.next]
            if p.random:
                d[p].random = d[p.random]
            p = p.next
        return d.get(head)
