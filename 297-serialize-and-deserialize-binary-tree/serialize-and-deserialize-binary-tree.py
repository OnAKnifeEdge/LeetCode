# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    SEP = ','
    NULL = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return self.NULL

        q = deque([root])
        r = []

        while q:
            node = q.popleft()

            if node:
                r.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                r.append(self.NULL)

        return self.SEP.join(r)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == self.NULL:
            return

        nodes = iter(data.split(self.SEP))
        root_value = next(nodes)
        root = TreeNode(int(root_value))

        q = deque([root])

        while q:
            node = q.popleft()

            if not node:
                continue

            left_val, right_val = next(nodes), next(nodes)

            if left_val != self.NULL:
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)
            
            if right_val != self.NULL:
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))