class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/editorial/
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for num in nums:
            idx = abs(num) - 1
            if 0 <= idx < n and nums[idx] > 0:
                nums[idx] *= -1

        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1
        return n + 1
