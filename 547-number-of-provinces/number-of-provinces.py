class UnionFind:

    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
        self.count = size

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = self.root[root_y]
        elif self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = self.root[root_x]
        else:
            self.root[root_y] = self.root[root_x]
            self.rank[root_x] += 1
        self.count -= 1

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def get_count(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i, j in itertools.combinations(range(n), 2):
            if isConnected[i][j]:
                uf.union(i, j)

        return uf.get_count()
