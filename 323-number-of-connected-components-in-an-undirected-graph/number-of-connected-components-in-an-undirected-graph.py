class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            while x != parent[x]:
                # path compression
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        rank = [0] * n
        count = n

        def union(a, b):
            nonlocal count
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return
            if rank[a] < rank[b]:
                parent[root_a] = root_b
            elif rank[a] > rank[b]:
                parent[root_b] = root_a
            else:
                parent[root_a] = root_b
                rank[root_b] += 1
            count -= 1

        for a, b in edges:
            union(a, b)

        return count

    def countComponents_uf(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = n

        def find(x):
            while x != parent[x]:
                # path compression
                parent[x] = find(parent[x])
            return parent[parent[x]]

        def union(a, b):
            nonlocal count
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b
                count -= 1

        for a, b in edges:
            union(a, b)

        return count
