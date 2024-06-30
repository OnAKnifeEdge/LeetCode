class UnionFind:

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return 
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_y] < self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
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

        for i, c in enumerate(s):
            root = uf.find(i)
            graph[root].append(c)

        graph = {k: sorted(v, reverse=True) for k, v in graph.items()}

        result = []
        for i in range(n):
            root = uf.find(i)
            result.append(graph[root].pop())

        return "".join(result)
