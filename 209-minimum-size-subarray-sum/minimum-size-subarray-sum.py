class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest = float("inf")
        running_sum = 0
        left = 0
        right = 0
        while right < len(nums):
            running_sum += nums[right]
            while running_sum >= target:
                smallest = min(smallest, right - left + 1)
                running_sum -= nums[left]
                left += 1
            right += 1
        return smallest if smallest != float("inf") else 0
