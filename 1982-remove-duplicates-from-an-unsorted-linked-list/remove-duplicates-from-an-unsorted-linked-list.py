# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        frequency = defaultdict(int)

        p = head
        while p:
            frequency[p.val] += 1
            p = p.next

        dummy = ListNode(0, head)
        p = dummy

        while p:
            unique = p.next
            while unique and frequency[unique.val] > 1:
                unique = unique.next
            p.next = unique
            p = p.next

        return dummy.next
