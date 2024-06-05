class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            result += [(1 << i) + x for x in reversed(result)]
        return result
