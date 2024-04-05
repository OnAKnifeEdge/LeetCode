class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[:] = map(list, zip(*matrix[::-1]))

        # matrix.reverse()
        # for i in range(len(matrix)):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # flip
        for row in matrix:
            for j in range(n // 2):
                row[j], row[~j] = row[~j], row[j]
