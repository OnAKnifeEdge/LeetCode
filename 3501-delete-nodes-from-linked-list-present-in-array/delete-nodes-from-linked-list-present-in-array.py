# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0, head)
        curr = dummy
        pre = dummy
        while curr:
            if curr.val in nums:
                pre.next = curr.next
            else:
                pre = curr
            curr = curr.next
        return dummy.next
