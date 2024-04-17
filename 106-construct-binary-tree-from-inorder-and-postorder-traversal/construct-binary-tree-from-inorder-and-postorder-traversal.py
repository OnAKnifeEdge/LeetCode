# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return

        d = {val: idx for idx, val in enumerate(inorder)}
        idx = len(postorder) -  1

        def build_subtree(left, right):
            if left > right:
                return
            nonlocal idx
            root_val = postorder[idx]
            idx -= 1  
            root = TreeNode(root_val)
            root_idx = d[root_val]
           
            root.right = build_subtree(root_idx + 1, right)
            root.left = build_subtree(left, root_idx - 1)
            
   
            return root
        
        return build_subtree(0, len(postorder) - 1)