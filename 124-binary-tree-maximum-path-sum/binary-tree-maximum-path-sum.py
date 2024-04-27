# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s = float("-inf")

        def findMaxPath(node: Optional[TreeNode]) -> int:
            nonlocal s
            if not node:
                return 0
            # Recursively find the maximum path sum of the left subtree, avoid negative paths.
            left = max(findMaxPath(node.left), 0)
            # Recursively find the maximum path sum of the right subtree, avoid negative paths.
            right = max(findMaxPath(node.right), 0)

            # The current node's max path could be the sum of itself and max paths through both subtrees.
            s = max(left + right + node.val, s)

            # Return the maximum value path including the node and one of its subtrees.
            return max(left + node.val, right + node.val)

        findMaxPath(root)
        return s
