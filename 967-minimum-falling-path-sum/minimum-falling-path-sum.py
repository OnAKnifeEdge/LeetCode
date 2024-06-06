class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 对于 matrix[i][j]
        # 只有可能从 matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1] 这三个位置掉下来

        @cache
        def dp(i, j):
            if j < 0 or j == len(matrix):
                return float("inf")

            if i == 0:
                return matrix[i][j]

            return min(dp(i - 1, j), dp(i - 1, j - 1), dp(i - 1, j + 1)) + matrix[i][j]

        result = float("inf")
        for j in range(len(matrix)):
            s = dp(len(matrix) - 1, j)
            result = min(result, s)

        return result
