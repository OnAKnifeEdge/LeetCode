from typing import List


class Solution:
    # https://leetcode.com/problems/maximum-subarray
    def max_sub_array(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_val = dp[0]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]
            max_val = max(max_val, dp[i])
        return max_val
