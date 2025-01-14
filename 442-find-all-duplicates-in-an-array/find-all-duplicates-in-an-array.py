class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
        # https://leetcode.com/problems/find-all-duplicates-in-an-array/
        # https://leetcode.com/problems/first-missing-positive/
        duplicates = []
        frequency = [False] * (len(nums) + 1)
        for num in nums:
            if frequency[num]:
                duplicates.append(num)
            else:
                frequency[num] = True
        return duplicates

     