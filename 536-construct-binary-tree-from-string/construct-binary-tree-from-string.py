# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        if s[-1].isdigit():
            return TreeNode(int(s))  # Handles single node tree.

        i = s.find("(")
        root = TreeNode(int(s[:i]))  # Finding root node.

        stack = 1  # the count of unmatched "("
        j = i
        while stack > 0:  # until all parentheses are properly matched
            j += 1
            if s[j] == "(":
                stack += 1
            elif s[j] == ")":
                stack -= 1
        # s[j] is the closing parenthesis for the left child's subtree string

        root.left = self.str2tree(s[i + 1:j])
        # j+2 is to move past the ")(", -1 is to exclude the last ")"
        root.right = self.str2tree(s[j + 2:-1])

        return root
