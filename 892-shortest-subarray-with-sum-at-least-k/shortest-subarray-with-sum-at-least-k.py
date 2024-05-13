class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # 1. prefix_sum
        # 2. mono_q on top of prefix_sum: diff >= k
        # 3. smallest window
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        mono_q = deque()
        # stores indices of prefix_sum so that it is increasing (including equals )
        # eg: nums = [3, -1, 2, 1, -1, 2] and k = 5.
        # prefix_sum [0, 3, 2, 4, 5, 4, 6]
        # if 5 -2 does not meet condition, 5 - 3 won't meet condition for sure.
        # the smallest will be prefix_sum val bigger than 2
        left = 0
        shortest = float("inf")
        for right in range(len(nums) + 1):
            while mono_q and prefix_sum[right] - prefix_sum[mono_q[0]] >= k:
                left = mono_q.popleft()
                shortest = min(shortest, right - left)

            while mono_q and prefix_sum[mono_q[-1]] > prefix_sum[right]:
                mono_q.pop()

            mono_q.append(right)
        return shortest if shortest != float("inf") else -1
