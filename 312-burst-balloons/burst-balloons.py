class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (len(nums) - 2) * nums[0] ** 3 + nums[0] ** 2 + nums[0]

        nums = [1] + nums + [1]
        n = len(nums)

        # dp[i][j] represents maxCoins if burst all from [i, j]

        dp = [[0] * n for _ in range(n)]

        # do not burst the fake ballons
        # 从下到上，从左到右
        for left in reversed(range(1, n - 1)):
            for right in range(left, n - 1):
                # find the last burst one in nums[left]...nums[right]
                for i in range(left, right + 1):
                    # nums[i] is the last burst one
                    gain = nums[left - 1] * nums[i] * nums[right + 1]
                    # recursively call left side and right side
                    remaining = dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(remaining + gain, dp[left][right])

        return dp[1][n - 2]