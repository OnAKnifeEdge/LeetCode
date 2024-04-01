# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# LeetCode 26: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     slow = 0
    #     fast = 1
    #     while fast < len(nums):
    #         if nums[fast] != nums[slow]:
    #             slow += 1
    #             nums[slow] = nums[fast]
    #         fast += 1
    #     return slow + 1


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head
        