class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        half = sum(nums) / 2
        curr, ways = 0, 0
        for n in nums[:-1]:
            curr += n
            ways += curr >= half
        return ways
