class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        longest = 0
        zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            longest = max(longest, right - left)
        return longest
