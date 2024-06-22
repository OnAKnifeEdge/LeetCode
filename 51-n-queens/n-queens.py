class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        state = [["."] * n for _ in range(n)]

        cols, diagonals, anti_diagonals = set(), set(), set()

        def flatten(matrix):
            return ["".join(row) for row in matrix]

        def is_valid(i, j):
            if j in cols:
                return False
            if i - j in diagonals:
                return False
            if i + j in anti_diagonals:
                return False
            return True

        def place_queen(i, j):
            state[i][j] = "Q"
            cols.add(j)
            diagonals.add(i - j)
            anti_diagonals.add(i + j)

        def remove_queen(i, j):
            state[i][j] = "."
            cols.remove(j)
            diagonals.remove(i - j)
            anti_diagonals.remove(i + j)

        def backtrack(i):
            if i == n:
                result.append(flatten(state))
                return

            for j in range(n):
                if not is_valid(i, j):
                    continue
                place_queen(i, j)
                backtrack(i + 1)
                remove_queen(i, j)

        backtrack(0)

        return result
