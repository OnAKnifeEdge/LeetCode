# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodes = []
        mono_stack = []
        n = 0
        while head:
            nodes.append(head.val)
            head = head.next
            n += 1
        result = [0] * n
        for i in reversed(range(len(nodes))):
            while mono_stack and mono_stack[-1] <= nodes[i]:
                mono_stack.pop()
            if mono_stack:
                result[i] = mono_stack[-1]
            mono_stack.append(nodes[i])
        return result
