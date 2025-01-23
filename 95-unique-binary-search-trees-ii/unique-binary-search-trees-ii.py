# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @cache
        def generate(lo, hi):
            result = []
            if lo > hi:
                result.append(None)
                return result
            for i in range(lo, hi + 1):
                
                left_trees = generate(lo, i - 1)
                right_trees = generate(i + 1, hi)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i, left, right)
                        result.append(root)
            return result

        return generate(1, n)
        


