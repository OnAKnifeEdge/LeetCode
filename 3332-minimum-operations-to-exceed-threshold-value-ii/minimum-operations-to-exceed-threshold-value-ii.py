class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        cnt = 0
        while nums[0] < k and len(nums) > 1:
            x = heappop(nums)
            y = heappop(nums)
            z = min(x, y) * 2 + max(x, y)
            heappush(nums, z)
            cnt += 1
        return cnt 
