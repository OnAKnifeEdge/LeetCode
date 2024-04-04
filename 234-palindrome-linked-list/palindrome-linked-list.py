# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            left, left.next, slow = slow, left, slow.next
        if fast:
            slow = slow.next
        while left and left.val == slow.val:
            slow = slow.next
            left = left.next
        
        return not left



    #     slow, fast = head, head

    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next

    #     left, right = head, self.reverse(slow)


    #     while right:
    #         if left.val != right.val:
    #             return False
    #         left = left.next
    #         right = right.next

    #     return True


    # def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     pre, curr = None, head
    #     while curr:
    #         nxt = curr.next
    #         curr.next = pre
    #         pre = curr
    #         curr = nxt
    #     return pre
        