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

        def serialize_helper(node):
            if not node:
                yield self.NULL
                return
            yield str(node.val)
            yield from serialize_helper(node.left)
            yield from serialize_helper(node.right)

        return self.SEP.join(serialize_helper(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(self.SEP))

        def deserialize_helper():
            val = next(values)
            if val == self.NULL:
                return 
            node = TreeNode(int(val))
            node.left = deserialize_helper()
            node.right = deserialize_helper()
            return node

        return deserialize_helper()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
