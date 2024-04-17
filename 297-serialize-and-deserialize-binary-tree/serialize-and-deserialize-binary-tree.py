# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    SEP = ","
    NULL = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.serialize_helper(root)

    def serialize_helper(self, root, s=""):
        if not root:
            s += self.NULL
            s += self.SEP
            return s

        s += str(root.val)
        s += self.SEP
        s = self.serialize_helper(root.left, s)
        s = self.serialize_helper(root.right, s)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(self.SEP)
        root = self.deserialize_helper(nodes)
        return root


    def deserialize_helper(self, nodes):
        if nodes[0] == self.NULL:
            nodes.pop(0)
            return

        root = TreeNode(nodes.pop(0))
        root.left = self.deserialize_helper(nodes)
        root.right = self.deserialize_helper(nodes)
        return root
        



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
