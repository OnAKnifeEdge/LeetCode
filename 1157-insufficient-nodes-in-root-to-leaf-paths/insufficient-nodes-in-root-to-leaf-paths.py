# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:

        def dfs(node, parent_sum=0):
            if not node:
                return None, float("-inf")
            curr_sum = parent_sum + node.val
            if not node.left and not node.right:
                if curr_sum >= limit:
                    return node, curr_sum
                else:
                    return None, curr_sum
            left, left_max = dfs(node.left, curr_sum)
            right, right_max = dfs(node.right, curr_sum)
            node.left = left
            node.right = right
            if not left and not right:
                return None, curr_sum

            return node, max(left_max, right_max)

        node, _ = dfs(root)
        return node
