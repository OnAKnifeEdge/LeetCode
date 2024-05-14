class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp[i] will store the maximum score you can get by reaching index i
        dp = [float("-inf")] * len(nums)
        dp[0] = nums[0]
        # dp[i] = nums[i] + max(dp[j] for j in range(max(0, i-k), i))
        mono_q = deque([0])  # decreasing dp[i]'s index
        for i in range(1, len(nums)):
            # Remove indices that are out of reach (more than k steps behind)
            while mono_q and mono_q[0] < i - k:
                mono_q.popleft()
            dp[i] = dp[mono_q[0]] + nums[i]
            # Everything smaller than the current dp val will be popped out
            while mono_q and dp[mono_q[-1]] < dp[i]:
                mono_q.pop()
            mono_q.append(i)
        return dp[-1]
