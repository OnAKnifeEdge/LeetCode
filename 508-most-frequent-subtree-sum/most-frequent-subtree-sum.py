# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        frequency = {}
        max_frequency = 0

        def get_tree_sum(node) -> int:
            nonlocal max_frequency
            if not node:
                return 0
            left = get_tree_sum(node.left)
            right = get_tree_sum(node.right)
            s = left + right + node.val
            frequency[s] = frequency.get(s, 0) + 1
            max_frequency = max(max_frequency, frequency[s])
            return s

        get_tree_sum(root)
        # max_frequency = max(frequency.values())
        return [f for f in frequency if frequency[f] == max_frequency]
