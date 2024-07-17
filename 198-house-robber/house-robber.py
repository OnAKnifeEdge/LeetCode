class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        a, b = 0, 0
        for i in range(len(nums)):
            a, b = b, max(a + nums[i], b)
        return b
