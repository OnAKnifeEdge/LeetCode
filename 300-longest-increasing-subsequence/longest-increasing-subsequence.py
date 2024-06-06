class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:  # increasing
        #             dp[i] = max(dp[j] + 1, dp[i])
        # return max(dp)

        # binary search
        # sub = []
        # for num in nums:
        #     i = bisect_left(sub, num)
        #     if i == len(sub):
        #         sub.append(num)
        #     else:
        #         sub[i] = num
        # return len(sub)

        # cards

        # if inputs are positive, we can use 0
        top = [float("inf")] * len(nums)

        piles = 0
        for num in nums:
            idx = bisect_left(top, num)
            if idx == piles:
                piles += 1
            top[idx] = num
        return piles
