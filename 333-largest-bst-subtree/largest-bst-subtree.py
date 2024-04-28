# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node:
                # so that left_max < node.val < right_min validates BST
                return float("inf"), float("-inf"), 0  # min, max, size
            left_min, left_max, left_size = helper(node.left)
            right_min, right_max, right_size = helper(node.right)

            if left_max < node.val < right_min:  # BST
                return (
                    min(left_min, node.val),
                    max(right_max, node.val),
                    left_size + right_size + 1,
                )
            # so that left_max > node.val and right_min < node.val invalidates BST
            return float("-inf"), float("inf"), max(left_size, right_size)

        _, _, s = helper(root)
        return s
