# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def traverse(node, parent_val, l):
            nonlocal max_length
            if not node:
                return
            if node.val == parent_val + 1:
                l += 1
            else:
                l = 1
            max_length = max(max_length, l)
            traverse(node.left, node.val, l)
            traverse(node.right, node.val, l)

        traverse(root, 0, 0)
        return max_length
        