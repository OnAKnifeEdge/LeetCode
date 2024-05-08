# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # idx = len(nums) // 2
        # root_val = nums[idx]
        # root = TreeNode(root_val)
        # root.left = self.sortedArrayToBST(nums[:idx])
        # root.right = self.sortedArrayToBST(nums[idx + 1:])
        # return root

        def build(start, end):
            if start > end:
                return
            idx = (start + end) // 2
            root_val = nums[idx]
            root = TreeNode(root_val)
            root.left = build(start, idx - 1)
            root.right = build(idx + 1, end)
            return root

        return build(0, len(nums) - 1)
