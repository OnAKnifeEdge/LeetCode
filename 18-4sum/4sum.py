class Solution:

    def k_sum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        result = []

        # nums are sorted

        if not nums:
            return result

        avg = target // k

        if avg < nums[0] or nums[-1] < avg:
            return result

        if k == 2:
            return self.two_sum(nums, target)

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for subset in self.k_sum(nums[i + 1:], target - nums[i], k - 1):
                result.append([nums[i]] + subset)
        return result

    def two_sum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif s > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                result.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum(nums, target, 4)
        