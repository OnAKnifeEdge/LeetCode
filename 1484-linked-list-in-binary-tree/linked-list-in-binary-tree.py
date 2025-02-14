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

        def is_sub_tree(head, node):
            if head is None:
                return True
            if node is None:
                return False
            if head.val != node.val:
                return False
            return is_sub_tree(head.next, node.left) or is_sub_tree(head.next, node.right)

        if not root or not head:
            return False
        return is_sub_tree(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)