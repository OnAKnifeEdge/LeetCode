class NumMatrix:

    # preSum[i][j] 记录 matrix 中子矩阵 [0, 0, i-1, j-1] 的元素和
    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])

        self.prefix_sum = [[0] * (C + 1) for _ in range(R + 1)]

        for i in range(R):
            for j in range(C):
                self.prefix_sum[i + 1][j + 1] = self.prefix_sum[i][j + 1] + self.prefix_sum[i + 1][j] + matrix[i][j] - self.prefix_sum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2 + 1][col2 + 1] - self.prefix_sum[row1][col2 + 1] - self.prefix_sum[row2 + 1][col1] + self.prefix_sum[row1][col1]


































        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)