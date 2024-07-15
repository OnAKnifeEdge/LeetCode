# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = defaultdict(list)
        nodes = set()
        children = set()
        for parent, child, is_left in descriptions:
            d[parent].append((child, is_left))
            nodes.add(parent)
            nodes.add(child)
            children.add(child)
        roots = nodes - children
        if len(roots) != 1:
            return None

        root = roots.pop()

        def dfs(val):
            node = TreeNode(val)
            for child, is_left in d[val]:
                if is_left:
                    node.left = dfs(child)
                else:
                    node.right = dfs(child)
            return node

        return dfs(root)
