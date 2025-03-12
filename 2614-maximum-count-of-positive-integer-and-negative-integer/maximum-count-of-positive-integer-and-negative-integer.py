class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives = self.left_bound(nums)
        positives = len(nums) - self.right_bound(nums)
        return max(negatives, positives)

    def left_bound(self, nums):  # find first non-negative value
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] < 0:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def right_bound(self, nums):  # find last positive value
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] > 0:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
