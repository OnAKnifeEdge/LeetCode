class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        d = {}
        max_length = 0
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (-1 if nums[i] == 0 else 1)

        for i in range(n + 1):
            s = prefix_sum[i]
            if s in d:
                max_length = max(max_length, i - d[s])
            else:
                d[s] = i
        return max_length
