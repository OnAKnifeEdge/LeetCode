class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # https://leetcode.com/problems/longest-well-performing-interval/submissions/1224328300/
        # https://leetcode.com/problems/contiguous-array/description/
        # 325
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        d = {}  # prefix_sum[i] % k: i
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        for i in range(n + 1):
            val = prefix_sum[i] % k
            if val not in d:
                d[val] = i

        for i in range(1, n + 1):
            target = prefix_sum[i] % k
            if target in d and i - d[target] >= 2:
                return True
        return False
