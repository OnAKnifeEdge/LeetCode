# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

NULL = '#'
SEP = ','

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return NULL
        nodes = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                nodes.append(NULL)
            else:
                nodes.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return SEP.join(nodes)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        if data == NULL:
            return None
        nodes = iter(data.split(SEP))
        root_val = next(nodes)
        root = TreeNode(int(root_val))

        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                continue
            left_val, right_val = next(nodes), next(nodes)
            if left_val != NULL:
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)
            if right_val != NULL:
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)
        return root
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))