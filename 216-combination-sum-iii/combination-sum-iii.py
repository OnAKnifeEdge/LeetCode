class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(i, s, path=[]):
            if s > n:
                return
            if len(path) == k and s == n:
                result.append(path[:])
                return
            for j in range(i + 1, 10):
                path.append(j)
                s += j
                backtrack(j, s, path)
                s -= j
                path.pop()

        backtrack(0, 0)
        return result
