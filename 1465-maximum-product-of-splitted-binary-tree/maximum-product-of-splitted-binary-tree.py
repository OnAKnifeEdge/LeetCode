# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        max_product = 0
        MOD = 10**9 + 7

        def get_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = get_sum(node.left)
            right = get_sum(node.right)
            return left + right + node.val

        total_sum = get_sum(root)

        def dfs(node: Optional[TreeNode]):
            nonlocal max_product
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            node_sum = left + right + node.val
            max_product = max(max_product, node_sum * (total_sum - node_sum))
            return node_sum

        dfs(root)
        return max_product % MOD
