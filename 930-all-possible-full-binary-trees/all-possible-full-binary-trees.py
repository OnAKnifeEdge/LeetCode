# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []

        return self.dp(n)

    @cache
    def dp(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode()]

        result = []

        for i in range(1, n, 2):
            left = self.dp(i)
            right = self.dp(n - 1 - i)

            for l_tree, r_tree in product(left, right):
                result.append(TreeNode(val=0, left=l_tree, right=r_tree))

        return result
