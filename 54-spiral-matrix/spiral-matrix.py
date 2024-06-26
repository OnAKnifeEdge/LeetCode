class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result.extend(matrix.pop(0))
            matrix = list(reversed([*zip(*matrix)]))
        
        return result
        