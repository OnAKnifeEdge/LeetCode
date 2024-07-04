# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        end = head.next
        running_sum = 0

        while end:
            if end.val == 0:
                node = ListNode(running_sum)
                start.next = node
                start = node
                running_sum = 0
            else:
                running_sum += end.val

            end = end.next

        return head.next
