# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # i: left tree, right tree
        inorder_map = {v: idx for idx, v in enumerate(inorder)}

        def build(pre_start, in_start, in_end): # idx is the preorder root idx
            if in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            inorder_root_idx = inorder_map[root_val]
            left_size = inorder_root_idx - in_start
            root.left = build(pre_start + 1, in_start, inorder_root_idx - 1)
            root.right = build(pre_start + 1 + left_size, inorder_root_idx + 1, in_end)
            return root

        return build(0, 0, len(preorder) - 1)
        