class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = 0
        left = 0
        smallest = float("inf")

        for right, num in enumerate(nums):
            running_sum += num
            while running_sum >= target:
                smallest = min(smallest, right - left + 1)
                running_sum -= nums[left]
                left += 1
        return smallest if smallest != float(inf) else 0
