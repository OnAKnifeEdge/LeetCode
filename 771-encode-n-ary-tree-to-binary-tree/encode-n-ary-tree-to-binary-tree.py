"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec:

    # Encodes an n-ary tree to a binary tree.
    """
    The encode method will convert the N-ary tree into a binary tree by:
    Setting the first child of an N-ary node as the left child of the binary node.
    Setting the siblings of the first child as a linked list
    using the right child pointer of the binary nodes.
    """

    def encode(self, root: "Optional[Node]") -> Optional[TreeNode]:
        if not root:
            return None

        binary_root = TreeNode(root.val)

        if not root.children:
            return binary_root

        first_child = root.children[0]
        binary_root.left = self.encode(first_child)

        current_node = binary_root.left
        for child in root.children[1:]:
            current_node.right = self.encode(child)
            current_node = current_node.right

        return binary_root

    # Decodes your binary tree to an n-ary tree.
    """
    The decode method will reverse this process:
    Reconstruct each N-ary node by gathering children
    starting from the binary node's left child.
    Siblings in the binary tree are determined by following the right child pointers.
    """

    def decode(self, binary_root: Optional[TreeNode]) -> "Optional[Node]":
        if not binary_root:
            return None

        root = Node(binary_root.val, children=[])

        current_node = binary_root.left
        while current_node:
            child = self.decode(current_node)
            root.children.append(child)
            current_node = current_node.right

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
