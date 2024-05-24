class Solution:

    def is_border(self, r, c, R, C):
        return r == 0 or c == 0 or r == R - 1 or c == C - 1

    class UnionFind:
        def __init__(self, size):
            self.parent = [i for i in range(size)]
            self.rank = [0 for _ in range(size)]

        def find(self, x):  # perform path compression
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):  # perform union by rank
            rx, ry = self.find(x), self.find(y)

            if rx != ry:  # if they are in different groups
                if self.rank[rx] < self.rank[ry]:  # include smaller rank to larger rank
                    self.parent[rx] = ry
                elif self.rank[rx] > self.rank[ry]:
                    self.parent[ry] = rx
                else:
                    self.parent[ry] = rx
                    self.rank[rx] += 1

    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        R, C = len(board), len(board[0])

        uf = self.UnionFind(R * C + 1)
        dummy = R * C

        def index(r, c):  # convert 2D coordinates to 1D
            return r * C + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r, c in itertools.product(range(R), range(C)):
            if board[r][c] != "O":
                continue
            if self.is_border(r, c, R, C):
                uf.union(index(r, c), dummy)
            else:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if board[nr][nc] == "O":
                        uf.union(index(r, c), index(nr, nc))

        for r, c in itertools.product(range(R), range(C)):
            # uf.find(dummy)
            #  group all boundary 'O's
            # uf.find(index(r, c))
            #  the representative of the current cell.
            if uf.find(dummy) == uf.find(index(r, c)):
                board[r][c] = "O"
            else:
                board[r][c] = "X"

    def solve_bfs(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        R = len(board)
        C = len(board[0])
        # 1. mark escape cells with any placeholder

        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                row, col = q.popleft()
                if not self.is_border(r, c, R, C):
                    continue
                if board[row][col] != "O":
                    continue
                board[row][col] = "E"
                q.append((row, col + 1))
                q.append((row, col - 1))
                q.append((row + 1, col))
                q.append((row - 1, col))

        for row, col in itertools.product(range(R), range(C)):
            if not self.is_border(r, c, R, C):
                continue
            bfs(row, col)

        # 2. flip captured cells to X and reset the placeholder back to O

        for r, c in itertools.product(range(R), range(C)):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "E":
                board[r][c] = "O"

    def solve_dfs(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        R = len(board)
        C = len(board[0])

        # 1. mark escape cells with any placeholder

        def dfs(r, c):
            if not self.is_border(r, c, R, C):
                return
            if board[r][c] != "O":
                return
            board[r][c] = "E"
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for row, col in itertools.product(range(R), range(C)):
            if not self.is_border(r, c, R, C):
                continue
            dfs(row, col)

        # 2. flip captured cells to X and reset the placeholder back to O

        for r, c in itertools.product(range(R), range(C)):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "E":
                board[r][c] = "O"
