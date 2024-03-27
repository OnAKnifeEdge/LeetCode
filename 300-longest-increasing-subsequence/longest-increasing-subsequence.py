class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        # dp[i] represents the length of the longest increasing subsequence that ends with the element at index i.
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: # increasing
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)