class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        i, j = entrance
        maze[i][j] = "+"  # Mark entrance as visited
        q = deque([(i, j, 0)])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            a, b, steps = q.popleft()
            for dx, dy in DIRECTIONS:
                x, y = a + dx, b + dy
                if 0 <= x < m and 0 <= y < n and maze[x][y] == ".":
                    if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                        return steps + 1
                    maze[x][y] = "+"  # Mark as visited
                    q.append((x, y, steps + 1))
        return -1
