# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = defaultdict(int)
        d[0] = 1  # prefix_sum == targetSum: 1

        def dfs(node, prefix_sum):  # return path_sum
            if not node:
                return 0
            prefix_sum += node.val
            count = d[prefix_sum - targetSum]
            d[prefix_sum] += 1
            left = dfs(node.left, prefix_sum)
            right = dfs(node.right, prefix_sum)
            count += left + right
            # After processing the left and right subtrees, 
            # we decrement the frequency of the current prefix_sum in d
            # to ensure that the d only contains prefix sums for the current path.
            d[prefix_sum] -= 1
            return count

        return dfs(root, 0)
