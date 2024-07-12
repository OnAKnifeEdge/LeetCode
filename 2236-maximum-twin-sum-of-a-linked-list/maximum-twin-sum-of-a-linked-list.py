# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = float("-inf")
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        def reverse(node):
            pre, curr = None, node
            while curr:
                curr.next, curr, pre = pre, curr.next, curr
            return pre

        r = reverse(slow)
        p = head

        while r:
            pair = p.val + r.val
            p = p.next
            r = r.next
            max_sum = max(max_sum, pair)
        return max_sum
