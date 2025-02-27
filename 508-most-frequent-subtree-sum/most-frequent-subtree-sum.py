# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        frequency = {}
        self.max_frequency = 0

        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            s = node.val + left_sum + right_sum
            frequency[s] = frequency.get(s, 0) + 1
            self.max_frequency = max(self.max_frequency, frequency[s])
            return s

        dfs(root)
        return [node for node in frequency if frequency[node] == self.max_frequency]
