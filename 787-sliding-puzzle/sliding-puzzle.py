class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # ROWS, COLS = len(board), len(board[0])
        # DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # m = ROWS * COLS

        # puzzle = [0] * (m)
        # neighbors = [0] * m

        # def to_idx(i, j):
        #     if i < 0 or j < 0 or i == ROWS or j == COLS:
        #         return None
        #     return i * COLS + j

        # def map_neighbors(i, j):
        #     neighbor = []
        #     for dx, dy in DIRECTIONS:
        #         idx = to_idx(i + dx, j + dy)
        #         if idx is not None:
        #             neighbor.append(idx)
        #     return neighbor

        # def flatten():
        #     for i in range(ROWS):
        #         for j in range(COLS):
        #             idx = to_idx(i, j)
        #             puzzle[idx] = board[i][j]
        #             neighbors[idx] = map_neighbors(i, j)

        # flatten()

        neighbors = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        puzzle = [*board[0], *board[1]]


        start = tuple(puzzle)
        end = (1, 2, 3, 4, 5, 0)

        q = deque([start])
        visited = set([start])
        step = 0

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node == end:
                    return step
                idx = node.index(0)
                for adj in neighbors[idx]:
                    current = list(node)
                    current[idx], current[adj] = current[adj], current[idx]  # Swap
                    new_node = tuple(current)
                    if new_node not in visited:
                        q.append(new_node)
                        visited.add(new_node)
            step += 1
        return -1
