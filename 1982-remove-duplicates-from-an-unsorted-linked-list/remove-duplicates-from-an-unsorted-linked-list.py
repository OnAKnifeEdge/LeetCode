# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        c = {} # val: count
        p = head
        while p:
            c[p.val] = c.get(p.val, 0) + 1
            p = p.next
        
        dummy = ListNode(0, head)
        p = dummy
        
        while p:
           unique = p.next
           while unique and c[unique.val] > 1:
                unique = unique.next
           p.next = unique
           p = p.next

        return dummy.next