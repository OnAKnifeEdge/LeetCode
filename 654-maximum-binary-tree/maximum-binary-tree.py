# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.build(nums)

    def build(self, nums: List[int], lo=0, hi=None) -> Optional[TreeNode]:
        if hi is None:
            hi = len(nums) - 1
        if lo > hi:
            return None
       
        max_index = lo

        for i in range(lo + 1, hi + 1):
            if nums[i] > nums[max_index]:
                max_index = i

        root = TreeNode(nums[max_index])
        root.left = self.build(nums, lo, max_index - 1)  # Left subtree
        root.right = self.build(nums, max_index + 1, hi)  # Right subtree
        return root

    def constructMaximumBinaryTreeOptimal(self, nums: List[int]) -> Optional[TreeNode]:
        node_stack = []
        for num in nums:
            current_node = TreeNode(num)
            while (
                node_stack and node_stack[-1].val < num
            ):  # when num is the max value, put everything before on the left
                current_node.left = node_stack.pop()

            if node_stack:
                node_stack[-1].right = current_node

            node_stack.append(current_node)

        return node_stack[0]
