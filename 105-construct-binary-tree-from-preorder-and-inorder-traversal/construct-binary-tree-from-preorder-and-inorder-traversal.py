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

        d = {val: idx for idx, val in enumerate(inorder)}

        idx = 0

        def build_subtree(start, end):
            nonlocal idx
            if start > end:
                return

            root_val = preorder[idx]
            root = TreeNode(root_val)

            idx += 1

            root_idx = d[root_val]

            root.left = build_subtree(start, root_idx - 1)
            root.right = build_subtree(root_idx + 1, end)

            return root
        
        return build_subtree(0, len(preorder) - 1)
