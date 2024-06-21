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
            # identifies the first non-overlapping job
            # that could potentially be selected after the current job,
            # ensuring no time conflicts.
            next_job_idx = bisect_left(startTime, end)
            dp[i] = max(dp[i + 1], dp[next_job_idx] + p)
        return dp[0]
