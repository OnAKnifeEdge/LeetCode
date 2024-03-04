class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k <= 0:
            raise Exception(f'invalid window size k={k}')
        running_sum = 0
        max_average = sum(nums[:k]) / k
        for i in range(len(nums)):
            running_sum += nums[i]
            average = running_sum / k
            if(i >= k - 1):
                if average > max_average:
                    max_average = average  
                running_sum -= nums[i - (k - 1)]
        return max_average
