class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
        # https://leetcode.com/problems/find-all-duplicates-in-an-array/
        # https://leetcode.com/problems/first-missing-positive/

        seen = [False] * len(nums)
        result = []
        for num in nums:
            if not seen[num - 1]:
                seen[num - 1] = True
            else:
                result.append(num)
        return result
