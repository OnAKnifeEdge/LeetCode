# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def count(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + count(root.left) + count(root.right)

        total = count(root)

        def dfs(node: Optional[TreeNode], idx: int) -> bool:
            nonlocal total
            if not node:
                return True
            """
            If at any point during the DFS traversal,
            you try to visit a node whose idx is greater than or equal to total_nodes,
            it would mean that
            a node supposedly exists beyond the count of actual nodes in the tree.
            This implies that the tree is not complete because either:
            There is a node missing in previous levels.
            Or there are nodes in the last level to the right of the last node

       1
      / \
     2   3
    / \
   4   5

       1
      / \
     2   3
    /     \
   4       6
            """
            if idx >= total:
                return False
            is_left_complete = dfs(node.left, idx * 2 + 1)
            is_right_complete = dfs(node.right, idx * 2 + 2)
            return is_left_complete and is_right_complete

        return dfs(root, 0)

    def isCompleteTreeBFS(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        # If we find any 'not-none' node after this spot, the tree isn't complete.
        found_empty = False

        while q:
            node = q.popleft()
            if not node:
                found_empty = True
            # found a 'not-none' node
            else:
                if found_empty:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
