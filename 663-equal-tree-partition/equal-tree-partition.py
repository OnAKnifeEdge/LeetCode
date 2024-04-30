# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sum_set = set()

        def dfs(node) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = left + node.val + right
            if node != root:
                sum_set.add(s)
            return s

        total = dfs(root)

        if total % 2 != 0:
            return False

        if total == 0:
            return 0 in sum_set

        # Check if a partition exists that equals half the total sum
        return (total // 2) in sum_set
