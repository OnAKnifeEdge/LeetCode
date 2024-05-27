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


class Point(NamedTuple):
    x: int
    y: int
    weight: int


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        p = []
        n = len(points)
        for i, j in itertools.combinations(range(n), 2):
            xi, yi = points[i]
            xj, yj = points[j]
            p.append(Point(x=i, y=j, weight=abs(xi - xj) + abs(yi - yj)))
        p.sort(key=lambda x: x.weight)

        mst = 0
        uf = UnionFind(n)
        for point in p:
            if uf.find(point.x) == uf.find(point.y):
                continue
            uf.union(point.x, point.y)
            mst += point.weight
        return mst
