# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_map = {v: idx for idx, v in enumerate(postorder)}
        n = len(preorder)
        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return
            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root
            left_root_val = preorder[pre_start + 1]
            post_left_root_idx = postorder_map[left_root_val]
            left_size = post_left_root_idx - post_start + 1
            root.left = build(pre_start + 1, pre_start + left_size, post_start, post_left_root_idx)
            root.right = build(pre_start + 1 + left_size, pre_end, post_left_root_idx  + 1, post_end - 1)
            return root
        return build(0, n - 1, 0, n - 1)

