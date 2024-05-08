# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        current = head

        def inorder(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            nonlocal current
            mid = (start + end) // 2
            left = inorder(start, mid - 1)
            root = TreeNode(current.val)
            current = current.next
            right = inorder(mid + 1, end)
            root.left = left
            root.right = right
            return root

        return inorder(0, n - 1)

    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        fast, slow, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if pre:
            pre.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
