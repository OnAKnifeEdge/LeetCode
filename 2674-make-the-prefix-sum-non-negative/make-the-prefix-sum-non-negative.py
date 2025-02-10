class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        prefix_sum = 0
        cnt = 0
        min_heap = []
        for i, num in enumerate(nums):
            prefix_sum += num
            heappush(min_heap, num)
            if prefix_sum < 0:
                prefix_sum -= heappop(min_heap)
                cnt += 1
        return cnt
