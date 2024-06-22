class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(current, s, start):
            if s == n and len(current) == k:
                result.append(current[:])
                return
            if s > n or len(current) > k:
                return
            for i in range(start, 10):
                current.append(i)
                backtrack(current, s + i, i + 1)
                current.pop()

        backtrack([], 0, 1)
        return result
