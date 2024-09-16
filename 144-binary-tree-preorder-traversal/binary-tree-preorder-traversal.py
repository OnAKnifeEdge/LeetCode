class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node is not None:
                result.append(node.val)
                stack.append(node.right)  # Push right first so left is processed next
                stack.append(node.left)  # Push left after right
        return result
