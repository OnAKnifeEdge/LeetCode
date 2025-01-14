class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/editorial/
        n = len(nums)
        for i, num in enumerate(nums):
            if num <= 0 or num > n:
                nums[i] = n + 1
        for num in nums:
            idx = abs(num) - 1
            if 0 <= idx < n and nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1
