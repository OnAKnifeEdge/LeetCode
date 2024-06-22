class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n

        def backtrack(current):
            if len(current) == n:
                result.append(current[:])
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                current.append(num)
                used[i] = True
                backtrack(current)
                current.pop()
                used[i] = False
            

        backtrack([])
        return result
        