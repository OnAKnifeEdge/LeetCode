# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(node, min_val, max_val) -> bool:
            if node is None:
                return True
            if min_val is not None and min_val >= node.val:
                return False
            if max_val is not None and max_val <= node.val:
                return False
            return is_valid(node.left, min_val, node.val) and is_valid(node.right, node.val, max_val)

        return is_valid(root, None, None)
