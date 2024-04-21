# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = ""

        def dfs(root, current):
            nonlocal smallest
            if not root:
                return 

            current = chr(root.val + ord('a')) + current

            if not root.left and not root.right:
                if not smallest or smallest > current:
                    smallest = current
            
            dfs(root.left, current)
            dfs(root.right, current)

        dfs(root, "")
        return smallest


        