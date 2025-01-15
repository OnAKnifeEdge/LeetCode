class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        block_sum = [[0] * COLS for _ in range(ROWS)]
        matrix = Matrix(mat)
        for i in range(ROWS):
            for j in range(COLS):
                x1 = max(0, i - k)
                x2 = min(ROWS - 1, i + k)
                y1 = max(0, j - k)
                y2 = min(COLS - 1, j + k)
                block_sum[i][j] = matrix.range_sum(x1, y1, x2, y2)
        return block_sum


class Matrix:
    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                self.prefix_sum[i][j] = self.prefix_sum[i - 1][j] + self.prefix_sum[i][j - 1] - self.prefix_sum[i - 1][j - 1] + matrix[i - 1][j - 1]

    def range_sum(self, x1, y1, x2, y2):
        return self.prefix_sum[x2 + 1][y2 + 1] - self.prefix_sum[x2 + 1][y1] - self.prefix_sum[x1][y2 + 1] + self.prefix_sum[x1][y1]
