# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0

        def traverse(root):
            nonlocal s
            if root is None:
                return
            traverse(root.right)
            s += root.val
            root.val = s
            traverse(root.left)
            return root

        return traverse(root)
        
        