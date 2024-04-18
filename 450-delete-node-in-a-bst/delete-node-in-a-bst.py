# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            # has left and right: replace with successor or replace with predecessor

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            successor = self.get_successor(root)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
            # root.right = self.deleteNode(root.right, successor.val)
            # successor.left = root.left
            # successor.right = root.right
            # return successor
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    def get_successor(self, node: Optional[TreeNode]) ->  Optional[TreeNode]:
        # The successor is the smallest node in the right subtree,
        # which is the leftmost child of the node's right subtree
        node = node.right
        while node.left:
            node = node.left
        return node

        
        