# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        if n % 2 == 0:
            return []

        cache = {0: [], 1: [TreeNode()]}  # map n: list of FBT

        def dp(n):
            if n in cache:
                return cache[n]

            result = []

            for i in range(1, n, 2):  # 0 to n - 1
                j = n - 1 - i
                left = dp(i)
                right = dp(j)

                for l in left:
                    for r in right:
                        result.append(TreeNode(val=0, left=l, right=r))
            cache[n] = result
            return result

        return dp(n)
