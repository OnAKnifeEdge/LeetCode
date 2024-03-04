class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k <= 0:
            raise Exception(f'invalid window size k={k}')
        running_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            running_sum += nums[i]
            running_sum -= nums[i - k]

            max_sum = max(max_sum, running_sum)

        return max_sum / k
