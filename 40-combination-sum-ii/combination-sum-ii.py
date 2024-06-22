class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        n = len(candidates)

        def backtrack(current, s, start):
            if s == target:
                result.append(current[:])
                return
            if s > target:
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]
                current.append(num)
                backtrack(current, s + num, i + 1)
                current.pop()

        backtrack([], 0, 0)
        return result
