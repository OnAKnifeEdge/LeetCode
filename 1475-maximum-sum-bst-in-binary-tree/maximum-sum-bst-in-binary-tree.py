# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        max_sum = float("-inf")

        def dfs(node):  # isBST, min, max, sum
            nonlocal max_sum

            min_val = float('inf')
            max_val = float('-inf')
            sum_val = 0

            if node is None:
                return True, min_val, max_val, sum_val

            is_left_bst, left_min, left_max, left_sum = dfs(node.left)
            is_right_bst, right_min, right_max, right_sum = dfs(node.right)

            if not is_left_bst or not is_right_bst:
                return False, min_val, max_val, sum_val

            if left_max < node.val < right_min:
                sum_val = node.val + left_sum + right_sum
                max_sum = max(max_sum, sum_val)
                return True, min(left_min, node.val), max(right_max, node.val), sum_val

            return False, min_val, max_val, sum_val

        dfs(root)
        return max(max_sum, 0)
