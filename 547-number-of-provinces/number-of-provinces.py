class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
        self.count = size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        # put the smaller one to the larger one
        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = self.root[root_y]
        elif self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = self.root[root_x]
        else:
            # root_y is attached to root_x if equals
            self.root[root_y] = self.root[root_x]
            self.rank[root_x] += 1
        self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_count(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        n = len(isConnected)

        uf = UnionFind(n)

        for i, j in itertools.combinations(range(n), 2):
            if isConnected[i][j] == 1:
                uf.union(i, j)

        return uf.get_count()
