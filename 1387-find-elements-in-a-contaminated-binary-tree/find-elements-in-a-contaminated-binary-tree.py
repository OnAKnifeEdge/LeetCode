# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set()
        if not root:
            return

        def build(node, val):
            if not node:
                return
            node.val = val
            self.nodes.add(val)
            build(node.left, 2 * val + 1)
            build(node.right, 2 * val + 2)

        build(root, 0)

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
