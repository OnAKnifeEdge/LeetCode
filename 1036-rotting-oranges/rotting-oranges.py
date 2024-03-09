class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0,1), (1, 0), (0, -1), (-1, 0)]
        fresh = 0
        time = 0
        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in DIRECTIONS:
                    r, c = x + dx, y + dy

                    if r < 0 or c < 0 or r == ROWS or c == COLS:
                        continue
                    
                    if grid[r][c] != 1:
                        continue
                    
                    grid[r][c] = 2
                    q.append((r, c))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1
