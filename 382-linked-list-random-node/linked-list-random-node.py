# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        if self.head is None:
            return None
        val = None
        current = self.head
        count = 1
        while current:
            if random.random() < 1 / count:
                val = current.val
            current = current.next
            count += 1
        return val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
