# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # step 1: find the middle -> it is the slow pointer
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # step 2: reverse the second half -> prev is the start
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # step 3: merge the two list
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

    def reorderListStack(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next

        p = head
        for _ in range(len(stack) // 2):
            last = stack.pop()
            last.next = p.next
            p.next = last
            p = last.next
        p.next = None
