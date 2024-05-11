# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodes = []
        mono_stack = []
        while head:
            nodes.append(head.val)
            head = head.next
        result = [0] * len(nodes)
        for i in reversed(range(len(nodes))):
            while mono_stack and mono_stack[-1] <= nodes[i]:
                mono_stack.pop()
            if mono_stack:
                result[i] = mono_stack[-1]
            mono_stack.append(nodes[i])
        return result
