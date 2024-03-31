# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        x = self.findNthFromEnd(dummy, n + 1)
        x.next = x.next.next
        return dummy.next


    def findNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        