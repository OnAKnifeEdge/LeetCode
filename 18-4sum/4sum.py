class Solution:

    def k_sum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        result = []

        # nums are sorted

        if not nums:
            return result

        # avg = target / k

        # if avg < nums[0] or nums[-1] < avg:
        #     return result

        if k == 2:
            return self.two_sum(nums, target)

        for i, num in enumerate(nums):
            # if num > target:
            #     break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for subset in self.k_sum(nums[i + 1:], target - nums[i], k - 1):
                result.append([nums[i]] + subset)
        return result

    def two_sum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            left = nums[lo]
            right = nums[hi]
            total = left + right
            if total < target:
                lo += 1
            elif total > target:
                hi -= 1
            else:
                result.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum(nums, target, 4)
