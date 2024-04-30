# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        avg = 0

        def get_cnt_and_sum(node: Optional[TreeNode]) -> Tuple[int, float]:
            nonlocal avg
            if not node:
                return 0, 0
            left_cnt, left_sum = get_cnt_and_sum(node.left)
            right_cnt, right_sum = get_cnt_and_sum(node.right)
            cnt = left_cnt + right_cnt + 1
            s = left_sum + right_sum + node.val
            avg = max(avg, s / cnt)
            return cnt, s

        get_cnt_and_sum(root)
        return avg
