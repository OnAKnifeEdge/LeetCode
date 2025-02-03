class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 1
        lo, hi = 0, 1
        longest = 1
        while hi < n:
            if nums[hi] > nums[hi - 1]:  # increasing
                longest = max(longest, hi - lo + 1)
            else:
                lo = hi
            hi += 1

        lo, hi = 0, 1
        while hi < n:
            if nums[hi] < nums[hi - 1]:  # decreasing
                longest = max(longest, hi - lo + 1)
            else:
                lo = hi
            hi += 1

        return longest
