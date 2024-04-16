# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        node_stack = []
        for num in nums:
            current_node = TreeNode(num)
            while node_stack and node_stack[-1].val < num:
                current_node.left = node_stack.pop()

            if node_stack:
                node_stack[-1].right = current_node

            node_stack.append(current_node)

        return node_stack[0]
        