# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        def build(lo, hi):
            if not nums:
                return

            if lo > hi:
                return
            
            idx = -1
            max_val = float('-inf')
            for i in range(lo, hi + 1):
                if nums[i] > max_val:
                    max_val = nums[i]
                    idx = i
            
            root = TreeNode(max_val)
            root.left = build(lo, idx - 1)
            root.right = build(idx + 1, hi)
            return root

        return build(0, len(nums) - 1)

            
