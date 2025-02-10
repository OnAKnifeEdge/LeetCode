class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

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

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        uf = UnionFind(n)
        for x, y in edges:
            if uf.connected(x, y):
                return False
            uf.union(x, y)
        return True
