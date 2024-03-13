class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(remain, combination, i):
            if remain == 0 and len(combination) == k:
                results.append(list(combination))
                return
            elif remain < 0 or len(combination) == k:
                return

            for num in range(i, 9):
                combination.append(num + 1)
                backtrack(remain - num - 1, combination, num + 1)
                combination.pop()

        backtrack(n, [], 0)
        return results
        