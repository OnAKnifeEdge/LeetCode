# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # result = []
        current = root

        prev_val = None
        streak = 0
        max_streak = 0
        modes = []

        while current:
            if not current.left:
                # result.append(current.val)

                ###
                if current.val == prev_val:
                    streak += 1
                else:
                    streak = 1
                    prev_val = current.val

                if streak > max_streak:
                    modes = [current.val]
                    max_streak = streak
                elif streak == max_streak:
                    modes.append(current.val)
                ###

                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                if not pre.right:
                    pre.right = current
                    current = current.left
                else:
                    # result.append(current.val)

                    ### duplicate as before ###
                    if current.val == prev_val:
                        streak += 1
                    else:
                        streak = 1
                        prev_val = current.val

                    if streak > max_streak:
                        modes = [current.val]
                        max_streak = streak
                    elif streak == max_streak:
                        modes.append(current.val)
                    ###

                    pre.right = None
                    current = current.right
        return modes
