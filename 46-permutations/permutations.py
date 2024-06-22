class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])

            for i, num in enumerate(nums):
                if used[i]:
                    continue
                current.append(num)
                used[i] = True
                backtrack(current)
                current.remove(num)
                used[i] = False

        backtrack([])
        return result
