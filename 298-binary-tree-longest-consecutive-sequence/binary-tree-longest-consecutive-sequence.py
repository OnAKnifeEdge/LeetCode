# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node):
            if node is None:
                return 0
            nonlocal longest
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            current = 1
            if node.left:
                if node.left.val == node.val + 1:
                    current = max(current, left_length + 1)
            if node.right:
                if node.right.val == node.val + 1:
                    current = max(current, right_length + 1)
            longest = max(longest, current)
            return current
        dfs(root)
        return longest

        