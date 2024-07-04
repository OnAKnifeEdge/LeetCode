# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         start = head
#         end = head.next
#         s = 0
#         while end:
#             
#             if end.val == 0:
#                 node = ListNode(s)
#                 node.next = end
#                 start.next = node
#                 start = end
#                 
#                 s = 0
#             else:
#                 s += end.val
            # end = end.next
#         return head.next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        start = head
        end = head.next
        s = 0
        

        while end:
            if end.val == 0:
                node = ListNode(s)
                start.next = node
                start = node
                s = 0
            else:
                s += end.val
            end = end.next

        return head.next
