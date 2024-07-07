class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        startTime.sort()

        dp = [0] * (n + 1)  # dp[i]: max profit from jobs[i:]

        for i in reversed(range(n)):
            start, end, p = jobs[i]
            # find next job that starts after end
            idx = bisect_left(startTime, end)

            # don't take jobs[i]: dp[i + 1]
            # take the jobs[i]: dp[idx] + p
            dp[i] = max(dp[i + 1], dp[idx] + p)
        return dp[0]
