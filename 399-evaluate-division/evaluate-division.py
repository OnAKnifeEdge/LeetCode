class UnionFind:
    def __init__(self):
        self.parent = {}  # Keeps track of the parent of each node
        self.weight = {}  # Keeps track of the ratio relative to the parent

    def find(self, x: str) -> Tuple[str, float]:
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
        # Path compression with ratio update
        if self.parent[x] != x:
            parent = self.parent[x]
            root, parent_weight = self.find(parent)
            self.parent[x] = root
            self.weight[x] *= parent_weight
        return self.parent[x], self.weight[x]

    def union(self, x: str, y: str, value: float):

        root_x, weight_x = self.find(x)
        root_y, weight_y = self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y
            self.weight[root_x] = value * weight_y / weight_x
        # Explanation: The statement self.weight[root_x] = value * weight_y / weight_x
        # ensures that when you move root_x to root_y, it keeps the ratio for connected components valid


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        uf = UnionFind()

        # Union operation with given equations and values
        for (a, b), value in zip(equations, values):
            uf.union(a, b, value)

        result = []
        # Answer the queries
        for a, b in queries:
            if a in uf.parent and b in uf.parent:
                root_a, ratio_a = uf.find(a)
                root_b, ratio_b = uf.find(b)
                if root_a == root_b:
                    result.append(ratio_a / ratio_b)
                else:
                    result.append(-1.0)
            else:
                result.append(-1.0)

        return result
