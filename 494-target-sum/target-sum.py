class Solution:
    def findTargetSumWays_top_down(self, nums: List[int], target: int) -> int:
        # dp(i, total)
        #  returns the number of ways to achieve total using nums[i:]
        @cache
        def dp(i, total):
            if i == len(nums):  # reached the end
                return 1 if total == target else 0
            return dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])

        return dp(0, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # subset sum
        # (sum of S1 - sum of S2) = target
        # (sum of S1 + sum of S2) = sum(nums)
        # sum(S1) = (target + sum(nums))/2
        d, m = divmod(target + sum(nums), 2)
        #  target >= -1000, sum(nums) <= 1000

        if m != 0 or d < 0:
            return 0

        dp = [0] * (d + 1)

        # There's 1 way to achieve a sum of 0 - by selecting no elements
        dp[0] = 1

        for num in nums:
            # Traverse the DP array from right to left
            # (to avoid updating an entry before it's used to calculate the next entry)
            for i in reversed(range(num, d + 1)):
                # Update the DP entry for the current sum
                dp[i] += dp[i - num]

        # The last entry in DP array is our answer - the number of ways to sum to d
        return dp[d]
