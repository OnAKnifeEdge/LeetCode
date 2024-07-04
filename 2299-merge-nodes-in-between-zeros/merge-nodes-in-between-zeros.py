# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         start = head
#         end = head.next
#         s = head.val
#         while end:
#             s += end.val
#             if end.val == 0:
#                 node = ListNode(s)
#                 node.next = end
#                 start.next = node
#                 start = end
#                 end = end.next
#                 s = 0
#             else:
#                 end = end.next
#         return head.next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = head
        start = head
        s = 0

        end = head.next

        while end:
            if end.val == 0:
                start.next = ListNode(s)
                start = start.next
                s = 0
            else:
                s += end.val
            end = end.next

        return head.next
