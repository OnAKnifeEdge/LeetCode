class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1
    
        @cache
        # dp(i, k): min difficulty when you start working on i-th job at day `k`
        def dp(i, k):
            # reach the last day
            # we put all the remaining jobs on this day
            # so we return the one with max difficulty
            if k == d: 
                return max(jobDifficulty[i:])
            # init min difficulty with inf 
            best = float('inf')
            # hardest is the max difficulty we've seen so far on day `k`
            # init current max with 0
            hardest = 0
            # for jobDifficulty like 6 5 4 3 2 1, 
            # we can have following ways to distribute them into two days
            # 6 | 5 4 3 2 1
            # 6 5 | 4 3 2 1 
            # 6 5 4 | 3 2 1
            # 6 5 4 3 | 2 1
            # 6 5 4 3 2 | 1
            # notice that each day we must have at least one task
            # given the starting index `i`, 
            # we can only at most choose the jobs till the position `n - d + k - 1`
            for j in range(i, n - (d - k)):
                hardest = max(hardest, jobDifficulty[j])
                # if j-th job is the last job on day `k`, 
                # the max difficulty for day `k` is `hardest`
                # and we need to start (j + 1)-th job on the next day
                # the result would be `hardest + dp(j + 1, k + 1)`
                # then we take the min
                best = min(best, hardest + dp(j + 1, k + 1))
            return best
        # n < d : you will have free days. hence you cannot find a schedule for the given jobs
        # e.g. Example 2
        # otherwise, we start working on 0-th job at day 1
        return dp(0, 1)