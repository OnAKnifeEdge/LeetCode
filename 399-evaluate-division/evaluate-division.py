class UnionFind:
    def __init__(self):
        self.root = {}
        self.weight = {}  # x/root
        # a/b = 2 and b/c = 3
        # a -> b with weight 2 (a = 2b)
        # b -> c with weight 3 (b = 3c)
        # So, a = 2b = 2(3c) = 6c, which allows us to answer queries like a/c = 6

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            self.weight[x] = 1.0

        if self.root[x] != x:
            root = self.find(self.root[x])
            self.weight[x] *= self.weight[self.root[x]]
            self.root[x] = root

        return self.root[x]

    def union(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        self.root[root_x] = root_y
        self.weight[root_x] = (self.weight[y] / self.weight[x]) * val
        # given x/y = val, x/root_x, y/root_y
        # root_x/root_y = ?
        # (y/root_y) / (x/root_x) = (root_x/root_y) * (y/x)

    def query(self, x, y):
        if x not in self.root or y not in self.root:
            return -1.0
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            return -1.0
        return self.weight[x] / self.weight[y]


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        uf = UnionFind()

        for (x, y), val in zip(equations, values):
            uf.union(x, y, val)

        result = []

        for x, y in queries:
            result.append(uf.query(x, y))

        return result
