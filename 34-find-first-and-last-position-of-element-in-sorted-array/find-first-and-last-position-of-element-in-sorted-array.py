class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1

        i = binarySearch()
        if i == -1:
            return [-1, -1]
        left, right = i, i

        while left > 0 and nums[left - 1] == target:
            left = left - 1
        while right < len(nums) -1 and nums[right + 1] == target:
            right = right + 1
        return [left, right]


        