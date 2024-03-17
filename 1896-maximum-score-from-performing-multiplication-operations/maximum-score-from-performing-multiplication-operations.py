class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # n, m = len(nums), len(multipliers)
        # dp = [[0] * (m + 1) for _ in range(0, m + 1)]

        # for i in range(m - 1, -1, -1):
        #     for left in range(i, -1, -1):
        #         right = n - 1 - (i - left)
        #         select_left = multipliers[i] * nums[left] + dp[i + 1][left + 1]
        #         select_right = multipliers[i] * nums[right] + dp[i + 1][left]
        #         dp[i][left] = max(select_left, select_right)

        # return dp[0][0]
        
        # space optimaztion
        n, m = len(nums), len(multipliers)
        dp = [0] * (m + 1)

        for i in range(m - 1, -1, -1):
            for left in range(0, i + 1):
                right = n - 1 - (i - left)
                select_left = multipliers[i] * nums[left] + dp[left + 1]
                select_right = multipliers[i] * nums[right] + dp[left]
                dp[left] = max(select_left, select_right)

        return dp[0]