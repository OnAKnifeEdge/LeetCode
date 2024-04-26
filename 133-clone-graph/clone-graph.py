"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
The main difference between cloning a connected undirected graph and cloning an N-ary tree lies in the structure and relationships between nodes:
Graph Structure:
In a connected undirected graph, any node can be connected to any other node, creating potential cycles and bidirectional connections. 
This means you need to handle back edges that could lead back to already processed nodes, as seen in the first problem.
Tree Structure:
An N-ary tree is a special kind of graph that has a hierarchical structure with no cycles. 
Each node has one parent (except the root) and zero or more children. There are no back edges to already processed ancestors, which makes the cloning process more straightforward because you don't have to worry about creating duplicate clones of the same node.
Node Definitions:
In the graph cloning problem, nodes have neighbors which represent bidirectional connections.
In the N-ary tree cloning problem, nodes have children, and this list represents all subtrees or descendants of that node. There are no back references to parents or siblings.
Traversal and Cloning Logic:
For the graph, since there are possible cycles, you must keep track of which nodes have already been visited to prevent cloning them multiple times.
For the tree, traditionally, you don't need to maintain a visited set since there's no possibility of revisiting the same node through different paths as there are no cycles.
"""
from typing import Optional


class Solution:

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        d = {}  # node: node_clone

        def copy(node):
            if not node:
                return None
            if node in d:
                return d[node]
            node_clone = Node(node.val, neighbors=[])
            d[node] = node_clone
            for neighbor in node.neighbors:
                node_clone.neighbors.append(copy(neighbor))
            return node_clone

        return copy(node)
