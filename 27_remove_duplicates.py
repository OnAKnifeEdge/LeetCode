from typing import List
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # less duplicates
    def remove_element(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        j = len(nums) - 1
        while i >= 0:
            if nums[i] != val:
                i = i - 1
            else:
                nums[i] = nums[j]
                i = i - 1
                j = j - 1
        return j + 1

    # lots of duplicates
    def remove_element_me(self, nums: List[int], val: int) -> int:
        i = 0
        for x in range(0, len(nums)):
            if nums[x] != val:
                nums[i] = nums[x]
                i = i + 1
        return i
