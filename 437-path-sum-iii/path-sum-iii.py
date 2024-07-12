# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = defaultdict(int)

        def dfs(node, prefix_sum):
            if not node:
                return 0
            prefix_sum += node.val
            count = d[prefix_sum - targetSum]
            if prefix_sum == targetSum:
                count += 1
            d[prefix_sum] += 1

            count += dfs(node.left, prefix_sum) + dfs(node.right, prefix_sum)

            d[prefix_sum] -= 1
            return count

        return dfs(root, 0)
