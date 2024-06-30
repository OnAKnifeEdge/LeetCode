class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_x, root_y = self.find(u), self.find(v)
        if root_x == root_y:
            return False

        if root_x < root_y:
            self.parent[root_x] = root_y
        elif root_y < root_x:
            self.parent[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        nm = n * m
        uf = UnionFind(nm)
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Correct directions

        def flatten(i, j):
            return i * m + j

        # cells_at_distance[i] stores cells at distance i from the nearest thief
        cells_at_distance = [[]]
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    cells_at_distance[0].append((i, j))
                    grid[i][j] = None

        # Calculate distances using BFS
        while grid[0][0] is not None and grid[-1][-1] is not None:
            current_level = cells_at_distance[-1]
            next_level = []
            cells_at_distance.append(next_level)

            for i, j in current_level:
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] is not None:
                        next_level.append((x, y))
                        grid[x][y] = None

        current_level = cells_at_distance.pop()
        for i, j in current_level:
            grid[i][j] = 0

        # Use Union-Find to check for a path from start to end
        for i in range(n):
            for j in range(m):
                if grid[i][j] is not None:
                    idx = flatten(i, j)
                    if i + 1 < n and grid[i + 1][j] is not None:
                        uf.union(idx, idx + m)
                    if j + 1 < m and grid[i][j + 1] is not None:
                        uf.union(idx, idx + 1)

        if uf.find(0) == nm - 1:
            return len(cells_at_distance)

        # Recover nodes in decreasing order of distance from thieves
        while cells_at_distance:
            current_level = cells_at_distance.pop()
            for i, j in current_level:
                grid[i][j] = 0
                idx = flatten(i, j)
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] is not None:
                        uf.union(idx, x * m + y)
            if uf.find(0) == nm - 1:
                break

        return len(cells_at_distance)
