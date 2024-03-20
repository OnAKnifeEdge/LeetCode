class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]: # increasing
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
        