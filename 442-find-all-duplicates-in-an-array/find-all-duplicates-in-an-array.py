class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
        # https://leetcode.com/problems/find-all-duplicates-in-an-array/
        # https://leetcode.com/problems/first-missing-positive/
        duplicates = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                duplicates.append(abs(num))
            else:
                nums[idx] = -nums[idx]

        return duplicates
