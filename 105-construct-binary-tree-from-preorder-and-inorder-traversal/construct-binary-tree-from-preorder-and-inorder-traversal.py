# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        d = {v: i for i, v in enumerate(inorder)} # inorder val: index dictionary

        def build(start, end):
            if start > end:
                return None
            root_val = preorder.pop(0)
            root_idx = d[root_val]
            root = TreeNode(root_val)
            root.left = build(start, root_idx - 1)
            root.right = build(root_idx + 1, end)
            return root

        return build(0, len(preorder) - 1)
        

        