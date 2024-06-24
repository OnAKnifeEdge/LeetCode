class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        buildings = 0
        min_distance = float("inf")

        # Store { total_dist, houses_count } for each cell.
        distances = [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]

        def bfs(r, c):

            q = deque([(r, c, 0)])
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] = True

            distance = 0

            while q:

                for _ in range(len(q)):
                    x, y, distance = q.popleft()
                    distance += 1
                    for dx, dy in DIRECTIONS:
                        i, j = x + dx, y + dy
                        if i < 0 or j < 0 or i == ROWS or j == COLS:
                            continue
                        if visited[i][j]:
                            continue
                        visited[i][j] = True

                        if grid[i][j] == 0:
                            distances[i][j][0] += distance
                            distances[i][j][1] += 1
                            q.append((i, j, distance))

        if not grid or not grid[0]:
            return -1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    buildings += 1
                    bfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and distances[r][c][1] == buildings:
                    min_distance = min(min_distance, distances[r][c][0])

        return min_distance if min_distance != float("inf") else -1
