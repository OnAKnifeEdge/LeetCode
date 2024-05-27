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
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[rx] = ry
            self.rank[ry] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        ds = UnionFind(n)
        connections.sort(key=lambda x: x[2])
        mst = 0
        num_edges = 0
        for a, b, w in connections:
            if ds.is_connected(a, b):
                continue
            mst += w
            ds.union(a, b)
            num_edges += 1
        return mst if num_edges == n - 1 else -1
