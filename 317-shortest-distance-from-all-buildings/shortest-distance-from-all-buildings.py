class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        if not grid[0]:
            return -1
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        distances = [[0] * COLS for _ in range(ROWS)]
        reached = [[0] * COLS for _ in range(ROWS)]

        buildings = 0

        def bfs(r, c):
            q = deque([(r, c, 0)])
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] = True
            while q:
                x, y, distance = q.popleft()
                for dx, dy in DIRECTIONS:
                    i, j = dx + x, dy + y
                    if i < 0 or j < 0 or i == ROWS or j == COLS:
                        continue
                    if visited[i][j]:
                        continue
                    if grid[i][j] == 0:
                        visited[i][j] = True
                        distances[i][j] += distance + 1
                        reached[i][j] += 1
                        q.append((i, j, distance + 1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    buildings += 1
                    bfs(i, j)

        min_distance = float("inf")
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 and reached[i][j] == buildings:
                    min_distance = min(min_distance, distances[i][j])

        if min_distance == float("inf"):
            return -1

        return min_distance
