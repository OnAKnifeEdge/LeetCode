class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = 0
        q = deque([])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        minutes = 0

        while q and fresh_count > 0:
            n = len(q)
            for _ in range(n):
                i, j = q.popleft()
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 1:
                        if grid[x][y] == 1:
                            fresh_count -= 1
                            grid[x][y] = 2
                        q.append((x, y))
            minutes += 1

        return minutes if fresh_count == 0 else -1
