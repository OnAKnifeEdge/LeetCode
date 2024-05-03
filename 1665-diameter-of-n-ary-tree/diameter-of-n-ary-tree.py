"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: "Node") -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        # the longest path in a tree can only happen between two leaves nodes or between a leaf node and the root node.
        # distance_through_node = height(child_m) + height(child_n)

        diameter = 0

        def height(node: "Node") -> int:
            nonlocal diameter
            if not node:
                return 0
            # leaf
            if not node.children:
                return 0

            longest, second_longest = 0, 0
            for child in node.children:
                h = height(child) + 1
                if h > longest:
                    longest, second_longest = h, longest
                elif h > second_longest:
                    second_longest = h

            diameter = max(diameter, longest + second_longest)
            return longest

        height(root)
        return diameter
