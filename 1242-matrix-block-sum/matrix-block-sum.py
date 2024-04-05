class Solution:
    # https://leetcode.com/submissions/detail/1223715446/
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        num_matrix = NumMatrix(mat)
        result = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                x1, y1 = max(i - k, 0), max(j - k, 0)
                x2, y2 = min(i + k, R - 1), min(j + k, C - 1)

                result[i][j] = num_matrix.sumRegion(x1, y1, x2, y2)
        return result


class NumMatrix:
    # every cell at (i+1, j+1) stores the sum of the submatrix from (0,0) to (i,j).
    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])

        self.prefix_sum = [[0] * (C + 1) for _ in range(R + 1)]

        for i in range(R):
            for j in range(C):
                val = (
                    self.prefix_sum[i][j + 1]
                    + self.prefix_sum[i + 1][j]
                    + matrix[i][j]
                    - self.prefix_sum[i][j]
                )

                self.prefix_sum[i + 1][j + 1] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )
