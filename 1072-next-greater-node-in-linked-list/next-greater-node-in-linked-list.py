# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = []
        mono_stack = []  # (i, val)
        i = 0

        while head:
            result.append(0)
            while mono_stack and mono_stack[-1][1] < head.val:
                idx, val = mono_stack.pop()
                result[idx] = head.val
            mono_stack.append((i, head.val))
            i += 1
            head = head.next
        return result
