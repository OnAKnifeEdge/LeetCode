class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        s = 0
        for num in nums:
            s += num
            self.prefix_sum.append(s)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
