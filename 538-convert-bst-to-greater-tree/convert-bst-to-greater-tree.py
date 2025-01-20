# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0
        def inorder(node):
            nonlocal s
            if node is None:
                return
            inorder(node.right)
            s += node.val
            node.val = s
            inorder(node.left)
        inorder(root)
        return root


        