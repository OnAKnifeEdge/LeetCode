# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(node, current=""):
            if not node:
                return None
            # Build current path by adding current node's letter
            current = chr(ord("a") + node.val) + current

            # If leaf node, return the path
            if not node.left and not node.right:
                return current

            # Recursively explore left and right subtrees
            left = dfs(node.left, current)
            right = dfs(node.right, current)

            # Compare paths lexicographically
            if left is None:
                return right
            if right is None:
                return left

            return min(left, right)

        return dfs(root)
