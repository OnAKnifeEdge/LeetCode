# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = {} # key triplet tuple: val count
        duplicates = []
        tree_id = 1
        trees = {} # key triplet tuple: val id

        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "0"
            left_id = serialize(node.left)
            right_id = serialize(node.right)
            subtree = (node.val, left_id, right_id)
            count[subtree] = count.get(subtree, 0) + 1

            if subtree not in trees:
                nonlocal tree_id
                trees[subtree] = tree_id
                tree_id += 1

            if count[subtree] == 2:
                duplicates.append(node)
            return trees[subtree]

        serialize(root)
        return duplicates
        