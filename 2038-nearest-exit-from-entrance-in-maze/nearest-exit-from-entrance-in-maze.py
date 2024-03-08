class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ex, ey = entrance
        maze[ex][ey] = '+'
        q = deque([(ex, ey, 0)])

        while q:
            for i in range(len(q)):
                x, y, d = q.popleft()

                for i, j in DIRECTIONS:
                    r = x + i
                    c = y + j
                    if 0 <= r < ROWS and 0 <= c < COLS and maze[r][c] == '.': 
                        if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                            return d + 1
                        maze[r][c] = '+'
                        q.append((r, c, d + 1))

        return -1
