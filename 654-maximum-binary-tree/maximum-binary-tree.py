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

        def build(start, end):
            if start > end:
                return None

            idx = start

            for i in range(start + 1, end + 1):
                if nums[i] > nums[idx]:
                    idx = i

            root_val = nums[idx]
            root = TreeNode(root_val)

            root.left = build(start, idx - 1)
            root.right = build(idx + 1, end)
            return root

        return build(0, len(nums) - 1)

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
