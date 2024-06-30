class UnionFind:
    def __init__(self, size):
        self.count = size
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        rank_x = self.rank[root_x]
        rank_y = self.rank[root_y]

        if rank_x < rank_y:  # x 是 小树， parent 指向 大树 y
            self.parent[root_x] = root_y
        elif rank_x > rank_y:  # y 是 小树， parent 指向 大树 x
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1
        self.count -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        removable_edges = 0

        # 1. process type 3
        for t, u, v in edges:
            if t == 3:
                a = uf_alice.union(u, v)
                b = uf_bob.union(u, v)
                if not a or not b:
                    removable_edges += 1

        # 2. process type 1 and 2
        for t, u, v in edges:
            if t == 1:
                if uf_alice.find(u) != uf_alice.find(v):
                    uf_alice.union(u, v)
                else:
                    removable_edges += 1
            if t == 2:
                if uf_bob.find(u) != uf_bob.find(v):
                    uf_bob.union(u, v)
                else:
                    removable_edges += 1
        if uf_alice.count != 2 or uf_bob.count != 2:
            return -1
        return removable_edges
