class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running_sum = sum(nums[:k])
        max_sum = running_sum
        for i in range(k, len(nums)):
            running_sum += nums[i]
            running_sum -= nums[i - k]
            max_sum = max(max_sum, running_sum)
        return max_sum / k
