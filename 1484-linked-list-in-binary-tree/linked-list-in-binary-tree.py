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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        if head.val == root.val and self.isSame(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isSame(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.isSame(head.next, root.left) or self.isSame(head.next, root.right)
