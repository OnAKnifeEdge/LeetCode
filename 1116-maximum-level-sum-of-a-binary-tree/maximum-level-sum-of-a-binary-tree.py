# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        level = 0

        q = deque([(root, 1)])
        while q:
            n = len(q)
            s = 0
            for _ in range(n):
                node, current_level = q.popleft()
                s += node.val
                if node.left:
                    q.append((node.left, current_level + 1))
                if node.right:
                    q.append((node.right, current_level + 1))
            if s > max_sum:
                max_sum = s
                level = current_level

        return level
