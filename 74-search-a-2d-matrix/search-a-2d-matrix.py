class Solution:
    def get(self, matrix: List[List[int]], idx: int) -> int:
        C = len(matrix[0])
        i, j = divmod(idx, C)
        return matrix[i][j]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        left, right = 0, R * C - 1

        while left <= right:
            mid = (left + right) // 2
            x = self.get(matrix, mid)
            if x == target:
                return True
            elif x < target:
                left = mid + 1
            else:
                right = mid - 1

        return False