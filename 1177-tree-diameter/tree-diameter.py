class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children else []

class Solution:



    def treeDiameter(self, edges: List[List[int]]) -> int:
        nodes = {}
        diameter = 0

        def build_tree() -> Dict:
            for edge in edges:
                for val in edge:
                    if val not in nodes:
                        nodes[val] = Node(val)

            for a, b in edges:
                nodes[a].children.append(nodes[b])
                nodes[b].children.append(nodes[a])

            return nodes

        def height(node: Node, parent: Node = None) -> int:
            nonlocal diameter
            longest, second_longest = 0, 0
            if not node:
                return 0
            if not node.children:
                return 0
            for child in node.children:
                if child is parent:
                    continue
                h = height(child, node) + 1
                if h > longest:
                    longest, second_longest = h, longest
                elif h > second_longest:
                    second_longest = h
            diameter = max(diameter, longest + second_longest)
            return longest

        build_tree()
        if not nodes:
            return 0
        height(nodes[0], None)
        return diameter
