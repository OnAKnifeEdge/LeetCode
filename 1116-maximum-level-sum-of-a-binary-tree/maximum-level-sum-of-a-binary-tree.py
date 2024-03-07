# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, result, level = float('-inf'), 0, 0

        if not root:
            return 0

        q = deque([root])

        while q:
            level += 1
            curr_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if max_sum < curr_sum:
                max_sum = curr_sum
                result = level
        return result
        