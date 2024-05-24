class Solution:

    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        R = len(board)
        C = len(board[0])

        # 1. find all border cells
        border_rows = [0, R - 1]
        border_cols = [0, C - 1]

        border_row_cells = list(itertools.product(range(R), border_cols))
        border_col_cells = list(itertools.product(border_rows, range(C)))

        borders = border_row_cells + border_col_cells

        # 2. mark escape cells with any placeholder

        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                row, col = q.popleft()
                if row < 0 or row == R:
                    continue
                if col < 0 or col == C:
                    continue
                if board[row][col] != "O":
                    continue
                board[row][col] = "E"
                q.append((row, col + 1))
                q.append((row, col - 1))
                q.append((row + 1, col))
                q.append((row - 1, col))

        for row, col in borders:
            bfs(row, col)

        # 3. flip captured cells to X and reset the placeholder back to O

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

        # 1. find all border cells
        border_rows = [0, R - 1]
        border_cols = [0, C - 1]

        border_row_cells = list(itertools.product(range(R), border_cols))
        border_col_cells = list(itertools.product(border_rows, range(C)))

        borders = border_row_cells + border_col_cells

        # 2. mark escape cells with any placeholder

        def dfs(r, c):
            if r < 0 or r == R:
                return
            if c < 0 or c == C:
                return
            if board[r][c] != "O":
                return
            board[r][c] = "E"
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for row, col in borders:
            dfs(row, col)

        # 3. flip captured cells to X and reset the placeholder back to O

        for r, c in itertools.product(range(R), range(C)):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "E":
                board[r][c] = "O"
