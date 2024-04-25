# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        d = defaultdict(int)  # {prefix_sum: count}

        def pre_order(node, prefix_sum):
            nonlocal count
            if not node:
                return
            prefix_sum += node.val

            if prefix_sum == targetSum:
                count += 1

            count = d[prefix_sum - targetSum] + count
            d[prefix_sum] = d[prefix_sum] + 1

            pre_order(node.left, prefix_sum)
            pre_order(node.right, prefix_sum)

            d[prefix_sum] = d[prefix_sum] - 1
        pre_order(root, 0)
        return count
