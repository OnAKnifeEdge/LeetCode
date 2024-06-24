class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        buildings = 0
        min_distance = float("inf")

        # Store { total_dist, houses_count } for each cell.
        distances = [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]

        def bfs(r, c):

            # Use a queue to do a BFS, starting from each cell located at (r, c).
            q = deque([(r, c)])
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] = True

            distance = 0

            while q:
                distance += 1
                for _ in range(len(q)):
                    x, y = q.popleft()

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
                            q.append((i, j))

        if not grid or not grid[0]:
            return -1

        # Count houses and start BFS from each house.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    buildings += 1
                    bfs(r, c)

        # Check all empty lands with house count equal to total houses and find the min ans.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and distances[r][c][1] == buildings:
                    min_distance = min(min_distance, distances[r][c][0])

        return min_distance if min_distance != float("inf") else -1
