class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def twoSum(i):
            lo = i + 1
            hi = len(nums) - 1

            while lo < hi:
                left = nums[lo]
                right = nums[hi]
                total = nums[i] + left + right
                if total < 0:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    continue
                elif total > 0:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                    continue
                result.append([nums[i], left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            twoSum(i)

        return result
