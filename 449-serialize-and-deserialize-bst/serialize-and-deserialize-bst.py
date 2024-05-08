# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    SEP = ","

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""

        def preorder(node):
            if not node:
                return []
            return [node.val] + preorder(node.left) + preorder(node.right)

        return self.SEP.join(map(str, preorder(root)))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
        """Decodes your encoded data to tree."""
        preorder = [int(x) for x in data.split(self.SEP) if data]

        def bst_from_preorder(preorder):
            if not preorder:
                return None
            root_val = preorder[0]
            root = TreeNode(root_val)
            right_idx = len(preorder)
            for i in range(1, len(preorder)):
                if preorder[i] > root_val:
                    right_idx = i
                    break
            root.left = bst_from_preorder(preorder[1:right_idx])
            root.right = bst_from_preorder(preorder[right_idx:])
            return root

        return bst_from_preorder(preorder)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
