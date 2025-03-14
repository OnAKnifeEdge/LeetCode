# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        result = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right  # Move to right subtree
        if not result:
            return []

        # Use Counter to find mode frequency
        freq = Counter(result)
        max_freq = max(freq.values())

        return [k for k, v in freq.items() if v == max_freq]