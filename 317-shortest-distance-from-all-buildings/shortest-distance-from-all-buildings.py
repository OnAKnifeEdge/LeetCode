class Solution:
    def bfs(self, grid, distances, row, col, totalHouses):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        # Use a queue to do a bfs, starting from each cell located at (row, col).
        q = deque([(row, col)])
        visited = [[False] * COLS for _ in range(ROWS)]
        visited[row][col] = True

        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and not visited[nx][ny]:
                        visited[nx][ny] = True

                        # If we reached an empty cell, then add the distance
                        # and increment the count of houses reached at this cell.
                        if grid[nx][ny] == 0:
                            distances[nx][ny][0] += steps
                            distances[nx][ny][1] += 1
                            q.append((nx, ny))

    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        totalHouses = 0
        minDistance = float("inf")

        # Store { total_dist, houses_count } for each cell.
        distances = [[[0, 0] for _ in range(cols)] for _ in range(rows)]

        # Count houses and start bfs from each house.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    totalHouses += 1
                    self.bfs(grid, distances, row, col, totalHouses)

        # Check all empty lands with houses count equal to total houses and find the min ans.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and distances[row][col][1] == totalHouses:
                    minDistance = min(minDistance, distances[row][col][0])

        return minDistance if minDistance != float("inf") else -1
