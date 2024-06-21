class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        startTime.sort()

        dp = [0] * (n + 1)

        for i in reversed(range(n)):
            start, end, p = jobs[i]
            idx = bisect_left(startTime, end)
            dp[i] = max(dp[i + 1], dp[idx] + p)
        return dp[0]
