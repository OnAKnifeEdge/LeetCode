class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]: # nums[left: mid] 有序
                if target >= nums[left] and target < nums[mid]: # target in range
                    right = mid - 1
                else:
                    left = mid + 1
                
            else: # nums[mid: right] 有序
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


        