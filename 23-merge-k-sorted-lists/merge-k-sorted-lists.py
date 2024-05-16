# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        ListNode.__lt__ = lambda self, other: self.val < other.val

        for head in lists:
            if not head:
                continue
            heappush(min_heap, head)

        dummy = ListNode()
        p = dummy
        while min_heap:
            node = heappop(min_heap)
            p.next = node
            p = p.next
            node = node.next
            if node:
                heappush(min_heap, node)
        return dummy.next
