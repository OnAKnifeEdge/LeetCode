# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node, max_so_far):
            nonlocal cnt
            if not node:
                return
            if node.val >= max_so_far:
                cnt += 1
            max_so_far = max(node.val, max_so_far)
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
        dfs(root, float('-inf'))
        return cnt