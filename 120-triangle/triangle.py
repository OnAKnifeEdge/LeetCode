class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        for i in reversed(range(n - 1)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]
