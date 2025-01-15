class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n)
        prefix_sum[0] = nums[0]
        count = 0
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        total = prefix_sum[-1]
        for i in range(n - 1):
            if prefix_sum[i] >= total - prefix_sum[i]:
                count += 1
        return count

        # half = sum(nums) / 2
        # curr, ways = 0, 0
        # for n in nums[:-1]:
        #     curr += n
        #     ways += curr >= half
        # return ways
