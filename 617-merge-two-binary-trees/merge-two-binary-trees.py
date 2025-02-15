from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        # Create a new root node for the merged tree
        merged_root = TreeNode(root1.val + root2.val)

        # Use a stack to keep track of nodes to process
        stack = [(root1, root2, merged_root)]

        while stack:
            node1, node2, merged_node = stack.pop()

            # Process left children
            left1 = node1.left if node1 else None
            left2 = node2.left if node2 else None
            if left1 or left2:
                # Calculate the value for the left child
                val1 = left1.val if left1 else 0
                val2 = left2.val if left2 else 0
                merged_node.left = TreeNode(val1 + val2)

                # Push the left children onto the stack
                stack.append((left1, left2, merged_node.left))

            # Process right children
            right1 = node1.right if node1 else None
            right2 = node2.right if node2 else None
            if right1 or right2:
                # Calculate the value for the right child
                val1 = right1.val if right1 else 0
                val2 = right2.val if right2 else 0
                merged_node.right = TreeNode(val1 + val2)

                # Push the right children onto the stack
                stack.append((right1, right2, merged_node.right))

        return merged_root
