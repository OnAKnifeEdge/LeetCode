class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/longest-well-performing-interval/submissions/1224328300/
        # https://leetcode.com/problems/contiguous-array/description/
        d = {}
        result = 0
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum == k:
                result = max(result, i + 1)
            if prefix_sum not in d:
                d[prefix_sum] = i
            if prefix_sum - k in d:
                result = max(result, i - d[prefix_sum-k])
        return result
