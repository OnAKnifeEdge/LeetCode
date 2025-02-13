
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        def find(root, x):
            if not root:
                return None
            if root.val == x:
                return root
            return find(root.left, x) or find(root.right, x)

        def count(node):
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)

        node = find(root, x)

        left = count(node.left)
        right = count(node.right)
        rest = n - left - right - 1
        return max(left, right, rest) > n // 2
