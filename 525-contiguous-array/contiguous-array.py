class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = 0
        d = {0: -1}

        max_length = 0

        for i in range(n):
            if nums[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum in d:
                max_length = max(max_length, i - d[prefix_sum])
            else:
                d[prefix_sum] = i

        return max_length
