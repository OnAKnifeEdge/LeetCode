class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/longest-well-performing-interval/submissions/1224328300/
        # https://leetcode.com/problems/contiguous-array/description/
        d = {0: -1}
        prefix_sum = 0
        max_length = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            target = prefix_sum - k
            if target in d:
                max_length = max(max_length, i - d[target])
            if prefix_sum not in d:
                d[prefix_sum] = i
        return max_length
