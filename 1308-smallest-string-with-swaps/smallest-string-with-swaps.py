class UnionFind:

    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.root[x] != x:
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
            self.root[root_x] = self.root[root_y]
            self.rank[root_y] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s
        n = len(s)
        uf = UnionFind(n)
        for x, y in pairs:
            uf.union(x, y)

        graph = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            graph[root].append(s[i])

        graph = {k: sorted(v, reverse=True) for k, v in graph.items()}

        result = [graph[uf.find(i)].pop() for i in range(n)]
        return "".join(result)
