from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[start] <= target or target <= nums[mid]:
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert solution.search(nums, 0) == 4
    assert solution.search(nums, 3) == -1
    assert solution.search(nums, 1) == 5
    assert solution.search([1, 3, 5], 5) == 2
    assert solution.search([5, 1, 3], 5) == 0
