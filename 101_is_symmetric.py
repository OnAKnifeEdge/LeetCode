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
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)

    # https://leetcode.com/problems/symmetric-tree/solution/236915

    def is_symmetric_2(self, root: TreeNode) -> bool:
        if root is None:
            return True
        q = [root.left, root.right]
        while q:
            node_1 = q.pop(0)
            node_2 = q.pop(0)
            if node_1 is None and node_2 is None:
                continue
            if node_1 is None or node_2 is None:
                return False
            if node_1.val != node_2.val:
                return False
            q.append(node_1.left)
            q.append(node_2.right)
            q.append(node_1.right)
            q.append(node_2.left)
        return True
