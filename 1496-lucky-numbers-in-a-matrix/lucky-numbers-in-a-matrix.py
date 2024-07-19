class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        row_min_max = float("-inf")
        for i in range(ROWS):
            row_min = min(matrix[i])
            row_min_max = max(row_min, row_min_max)

        col_max_min = float("inf")
        for j in range(COLS):
            col_max = max(matrix[i][j] for i in range(ROWS))
            col_max_min = min(col_max, col_max_min)

        if row_min_max == col_max_min:
            return [row_min_max]
        else:
            return []
