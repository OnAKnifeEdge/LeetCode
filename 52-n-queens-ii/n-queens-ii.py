class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0

        cols, diagnols, anti_diagnols = set(), set(), set()

        def is_valid(i, j):
            if j in cols:
                return False
            if i - j in diagnols:
                return False
            if i + j in anti_diagnols:
                return False
            return True

        def place_queen(i, j):
            cols.add(j)
            diagnols.add(i - j)
            anti_diagnols.add(i + j)

        def remove_queen(i, j):
            cols.remove(j)
            diagnols.remove(i - j)
            anti_diagnols.remove(i + j)

        def backtrack(i):
            nonlocal count
            if i == n:
                count += 1
                return

            for j in range(n):
                if not is_valid(i, j):
                    continue
                place_queen(i, j)
                backtrack(i + 1)
                remove_queen(i, j)

        backtrack(0)
        return count
