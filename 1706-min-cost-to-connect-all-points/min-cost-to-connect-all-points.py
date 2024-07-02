class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [0] * (size + 1)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        n = len(points)
        edges = []
        for i, j in combinations(range(n), 2):
            distance = manhattan(points[i], points[j])
            edges.append((i, j, distance))
        edges.sort(key=lambda x: x[2])

        mst = 0
        uf = UnionFind(n)
        for i, j, distance in edges:
            if uf.is_connected(i, j):
                continue
            uf.union(i, j)
            mst += distance
        return mst
