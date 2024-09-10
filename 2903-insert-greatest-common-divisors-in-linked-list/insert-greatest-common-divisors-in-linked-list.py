# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        a = head
        while a and a.next:
            b = a.next
            val = gcd(a.val, b.val)
            node = ListNode(val)
            a.next = node
            node.next = b
            a = b
            b = a.next
        return head
