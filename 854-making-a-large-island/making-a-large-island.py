class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.count = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            # x is the smaller tree
            self.parent[root_x] = root_y
            self.count[root_y] += self.count[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            # y is the smaller tree
            self.parent[root_y] = root_x
            self.count[root_x] += self.count[root_y]
        else:
            self.parent[root_y] = root_x
            self.count[root_x] += self.count[root_y]
            self.rank[root_x] += 1
        return True


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def flatten(i, j):
            """Maps 2D grid coordinates (i, j) to a 1D Union-Find index."""
            return i * n + j

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in DIRECTIONS:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            uf.union(flatten(i, j), flatten(x, y))

        max_area = max(uf.count)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_islands = set()
                    for dx, dy in DIRECTIONS:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            root = uf.find(flatten(x, y))
                            neighbor_islands.add(root)

                    potential_area = 1
                    for island_root in neighbor_islands:
                        potential_area += uf.count[island_root]

                    max_area = max(max_area, potential_area)

        return max_area
