class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def backtrack(current, s, start):
            if s == target:
                result.append(current[:])
                return
            elif s > target:
                return
            for i in range(start, n):
                num = candidates[i]
                current.append(num)
                backtrack(current, s + num, i)
                current.pop()

        backtrack([], 0, 0)
        return result
