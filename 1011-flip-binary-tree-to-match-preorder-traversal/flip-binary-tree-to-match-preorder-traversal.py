# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flipped = []
        idx = 0

        def dfs(node):
            nonlocal idx, flipped
            if not node:
                return
            if flipped and flipped[0] == -1:
                return
            if node.val != voyage[idx]:
                flipped = [-1]
                return
            idx += 1
            if idx < len(voyage) and node.left and node.left.val != voyage[idx]:
                flipped.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return flipped