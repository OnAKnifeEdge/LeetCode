# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # right tree min value
    def successor(self, root: TreeNode) -> int:
        # 下一个大的数：右的最左
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    # left tree max value
    def predecessor(self, root: TreeNode) -> int:
        # 上一个小的数：左的最右
        root = root.left
        while root.right:
            root = root.right
        return root.val
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                # 下一个大的数：右的最左
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                # 上一个小的数：左的最右
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
        