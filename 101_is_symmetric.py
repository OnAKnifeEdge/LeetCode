import TreeNode


class Solution:
    def is_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and (
            self.is_mirror(left.right, right.left)) and (
                   self.is_mirror(left.left, right.right))

    def is_symmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
