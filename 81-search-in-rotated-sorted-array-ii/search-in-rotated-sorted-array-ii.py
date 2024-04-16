class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:


            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1


            mid = (left + right) // 2

            if nums[mid] == target:
                return True
                
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
        return False
        