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

        """

        Suppose your `nums` array is `[1, 2, 3]`, and your goal (`d`) is `3`. We need to calculate the number of ways to achieve all sums up to `3` using these numbers.

        Initial `dp` array: `[1, 0, 0, 0]` (1 way to make sum `0`: by choosing no numbers)

        ### Right-to-Left Iteration (Correct)
        Let's start with `num = 1` (first iteration):

        - `dp` before iteration: `[1, 0, 0, 0]`
        - Updating `dp[i]` for each `i` in `reversed(range(1, 4))`: `i` goes `3, 2, 1`
            - `dp[3]` becomes `0 + dp[2]` (previous dp[3] plus dp[2]), dp does not change this pass since dp[2] is currently 0.
            - `dp[2]` becomes `0 + dp[1]` (previous dp[2] plus dp[1]), dp does not change this pass since dp[1] is currently 0.
            - `dp[1]` becomes `0 + dp[0]` (previous dp[1] plus dp[0]), so `dp[1] = 1`.
        - `dp` after first iteration: `[1, 1, 0, 0]`

        Next `num` is `2` (second iteration):

        - `dp` before iteration: `[1, 1, 0, 0]`
        - Updating `dp[i]` for each `i` in `reversed(range(2, 4))`: `i` goes `3, 2`
            - `dp[3]` becomes `0 + dp[1]`, so `dp[3] = 1`.
            - `dp[2]` becomes `0 + dp[0]`, so `dp[2] = 1`.
        - `dp` after second iteration: `[1, 1, 1, 1]`

        And so on for `num = 3`. Only after `num` is processed do we update `dp[i]`, so we're always using the untainted, original counts.

        ### Left-to-Right Iteration (Incorrect)

        Let's again start with `num = 1` (first iteration):

        - `dp` before iteration: `[1, 0, 0, 0]`
        - Updating `dp[i]` for each `i` in `range(1, 4)`: `i` goes `1, 2, 3`
            - `dp[1]` becomes `0 + dp[0]`, so `dp[1] = 1`.
            - `dp[2]` becomes `0 + dp[1]` (which was just updated), so `dp[2] = 1`.
            - `dp[3]` becomes `0 + dp[2]` (which was just updated), so `dp[3] = 1`.
        - `dp` after first iteration: `[1, 1, 1, 1]`

        Notice here that after immediately updating `dp[1]`, we used that new value to calculate `dp[2]`, and the same for `dp[3]`, which means we’ve effectively counted `num = 1` multiple times, which is incorrect.

        This is why traversing the array in reverse is crucial. By going right-to-left, we always use the state of the `dp` array before the current `num` is considered, ensuring that each number is only counted once for each sum.
        """
