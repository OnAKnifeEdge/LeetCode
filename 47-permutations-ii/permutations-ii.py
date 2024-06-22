class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        used = [False] * n

        def backtrack(current):
            if len(current) == n:
                result.append(current[:])
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue
                current.append(num)
                used[i] = True
                backtrack(current)
                current.pop()
                used[i] = False

        backtrack([])
        return result
