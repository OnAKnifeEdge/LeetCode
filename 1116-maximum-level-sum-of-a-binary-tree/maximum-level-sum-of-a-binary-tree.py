# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        level = 0
        max_level_sum = root.val
        min_level = 1
        while q:
            level += 1
            total = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if total > max_level_sum:
                max_level_sum = total
                min_level = level

        return min_level
