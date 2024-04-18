# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def generate(self, start, end, memo):
        result = []
        if start > end:
            result.append(None)
            return result
        if (start, end) in memo:
            return memo[(start, end)]
        
        for i in range(start, end + 1):
            left = self.generate(start, i - 1, memo)
            right = self.generate(i + 1, end, memo)

            for l in left:
                for r in right:
                    root = TreeNode(i, l, r)
                    result.append(root)

        memo[(start, end)] = result
        return result


    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.generate(1, n, memo)
        