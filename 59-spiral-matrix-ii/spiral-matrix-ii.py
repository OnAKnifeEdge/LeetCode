class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []
        
        matrix = [[0] * n for _ in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        
        val = 1

        while left <= right:

            for i in range(left, right):
                matrix[top][i] = val
                val += 1
            top += 1

            for i in range(top, bottom):
                matrix[i][right - 1] = val
                val += 1
            right -= 1

            for i in reversed(range(left, right)):
                matrix[bottom - 1][i] = val
                val += 1
            bottom -= 1

            for i in reversed(range(top, bottom)):
                matrix[i][left] = val
                val += 1
            left += 1
            
        return matrix
        