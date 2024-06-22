class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(current, start):
            if len(current) == k:
                result.append(current[:])
                return

            for num in range(start, n + 1):
                current.append(num)
                backtrack(current, num + 1)
                current.pop()

        backtrack([], 1)
        return result

        