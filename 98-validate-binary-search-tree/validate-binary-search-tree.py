# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, min_node, max_node):
            if not root:
                return True
            if min_node and root.val <= min_node.val:
                return False
            if max_node and root.val >= max_node.val:
                return False
            return helper(root.left, min_node, root) and helper(root.right, root, max_node)

        return helper(root, None, None)
        