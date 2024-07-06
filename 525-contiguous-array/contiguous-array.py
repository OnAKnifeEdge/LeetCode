class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        max_length = 0
        cumulative_diff = 0

        for i, num in enumerate(nums):
            if num == 1:
                cumulative_diff += 1
            elif num == 0:
                cumulative_diff -= 1
            if cumulative_diff == 0:  # find a target
                max_length = max(max_length, i + 1)
            else:
                if cumulative_diff in d:
                    max_length = max(max_length, i - d[cumulative_diff])
                else:
                    d[cumulative_diff] = i
        return max_length
