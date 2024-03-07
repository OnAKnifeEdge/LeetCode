# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/subarray-sum-equals-k/solutions/3777004/why-sum-k-read-this-to-understand/
class Solution:
    def pathSum(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        d = {}
        def preorder(node: Optional[TreeNode], prefix_sum: int) -> None:
            nonlocal count
            if not node:
                return None
            
            prefix_sum += node.val

            if prefix_sum == k:
                count += 1

            count += d.get(prefix_sum - k, 0)
            d[prefix_sum] = d.get(prefix_sum, 0) + 1

            preorder(node.left, prefix_sum)
            preorder(node.right, prefix_sum)

            d[prefix_sum] = d.get(prefix_sum, 0) - 1

        preorder(root, 0)
        return count
        