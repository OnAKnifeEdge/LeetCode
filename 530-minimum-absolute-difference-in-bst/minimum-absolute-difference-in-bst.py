# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_diff = float("inf")
        prev_val = None

        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if prev_val is not None:
                min_diff = min(abs(prev_val - node.val), min_diff)
            prev_val = node.val

            node = node.right
        
        return min_diff