class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp[i] 表示以 nums[i] 结尾的 subsequence 的 max_sum
        dp = [0] * len(nums)
        dp[0] = nums[0]
        # dp[i] = nums[i] + max(0, dp[i - j]) for j in [1, i - k]
        mono_deque = deque([0])  # [0] has the max value (idx of dp)
        # dp[j] smaller than the current dp[i] will be popped out
        for i in range(1, len(nums)):
            while mono_deque and mono_deque[0] < i - k:
                mono_deque.popleft()
            dp[i] = max(0, dp[mono_deque[0]]) + nums[i]
            while mono_deque and dp[mono_deque[-1]] < dp[i]:
                mono_deque.pop()
            mono_deque.append(i)
        return max(dp)
