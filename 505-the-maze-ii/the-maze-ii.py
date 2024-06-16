class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        distance = [[float("inf")] * COLS for _ in range(ROWS)]
        distance[start[0]][start[1]] = 0
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque([start])

        while q:
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                count = 0
                # Keep rolling until hitting a wall
                new_x, new_y = x, y
                while (
                    0 <= new_x + dx < ROWS
                    and 0 <= new_y + dy < COLS
                    and maze[new_x + dx][new_y + dy] == 0
                ):
                    new_x += dx
                    new_y += dy
                    count += 1

                if distance[x][y] + count < distance[new_x][new_y]:
                    distance[new_x][new_y] = distance[x][y] + count
                    if [new_x, new_y] != destination:
                        q.append([new_x, new_y])

        if distance[destination[0]][destination[1]] == float("inf"):
            return -1
        return distance[destination[0]][destination[1]]
