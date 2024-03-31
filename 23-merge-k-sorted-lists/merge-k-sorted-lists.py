# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # https://leetcode.com/problems/merge-k-sorted-lists/solutions/1447503/python-3-solutions-merge-2-linked-list-divide-and-conquer-priority-queue-clean-concise
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        ListNode.__lt__ = lambda self, other: self.val < other.val

        for l in lists:
            if not l:
                continue
            heappush(min_heap, l)

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