# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        inorder_map = {v: i for i, v in enumerate(inorder)}

        def build(idx, lo, hi):
            if lo > hi:
                return
            root_val = preorder[idx]
            root = TreeNode(root_val)
            inorder_root_idx = inorder_map[root_val]
            left_size = inorder_root_idx - lo
            root.left = build(idx + 1, lo, inorder_root_idx - 1)
            root.right = build(idx + left_size + 1, inorder_root_idx + 1, hi)
            return root
        return build(0, 0, len(preorder)- 1)

     