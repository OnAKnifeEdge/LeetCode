# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        critical_points = []

        prev = head
        node = head.next

        i = 1

        while node and node.next:
            if prev.val < node.val and node.val > node.next.val:
                critical_points.append(i)
            elif prev.val > node.val and node.val < node.next.val:
                critical_points.append(i)
            prev = node
            node = node.next
            i += 1

        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float("inf")
        for a, b in pairwise((critical_points)):
            min_distance = min(min_distance, b - a)

        max_distance = critical_points[-1] - critical_points[0]

        return [min_distance, max_distance]
