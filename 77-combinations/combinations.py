class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(candidate, idx):
            if len(candidate) == k:
                combinations.append(candidate[:])
                return

            for num in range(idx, n + 1):
                candidate.append(num)
                backtrack(candidate, num + 1)
                candidate.pop()

        backtrack([], 1)
        return combinations
