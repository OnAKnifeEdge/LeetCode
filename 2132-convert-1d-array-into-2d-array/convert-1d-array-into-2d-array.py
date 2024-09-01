class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        cnt = len(original)
        if m * n != cnt:
            return []
        result = [[0] * n for _ in range(m)]
        for i, num in enumerate(original):
            r, c = divmod(i, n)
            result[r][c] = num
        return result
