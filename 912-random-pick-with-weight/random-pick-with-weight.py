class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.prefix_sum = [0] * (self.n + 1)
        self.rand = random.Random()
        for i in range(1, len(self.prefix_sum)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i - 1]
        
    def pickIndex(self) -> int:
        target = self.rand.randint(1, self.prefix_sum[-1])
        return self.left_bount(self.prefix_sum, target) - 1

    def left_bount(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 1, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()