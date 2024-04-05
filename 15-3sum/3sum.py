class Solution:

    def twoSum(self, nums: List[int], i: int, result: List[List[int]])  -> List[List[int]]:
        # nums is sorted
        lo, hi = i + 1, len(nums) - 1

        while lo < hi:
            left, right = nums[lo], nums[hi]
            s = left + right + nums[i]
            if s < 0:
                lo += 1
                continue
                # while lo < hi and nums[lo] == left:
                #     lo += 1
                # continue
            elif s > 0:
                hi -= 1
                continue
                # while lo < hi and nums[hi] == right:
                #     hi -= 1
                # continue
            result.append([nums[i], left, right])
            while lo < hi and nums[lo] == left:
                lo += 1
            while lo < hi and nums[hi] == right:
                hi -= 1
        return result
            

    def threeSum(self, nums: List[int]) -> List[List[int]]:      
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result)
        return result

      