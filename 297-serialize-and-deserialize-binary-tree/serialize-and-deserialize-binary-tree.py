# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

SEP = ","
NULL = "#"

class Codec:


    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return NULL + SEP
        return self.serialize(root.left) + self.serialize(root.right) + str(root.val) + SEP

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(SEP)
        # Remove the last empty element due to the final separator
        nodes.pop()
        # We will use an iterator to make the deserialization cleaner
        return self.deserialize_helper(nodes)

    def deserialize_helper(self, nodes):
        val = nodes.pop()
        if val == NULL:
            return None
        root = TreeNode(int(val))
        # Postorder: First, build the right subtree, then the left subtree, then the node
        root.right = self.deserialize_helper(nodes)
        root.left = self.deserialize_helper(nodes)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
