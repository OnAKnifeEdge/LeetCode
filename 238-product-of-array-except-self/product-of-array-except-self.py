class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        product = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in reversed(range(n - 1)):
            right[i] = right[i + 1] * nums[i + 1]
        return [a * b for a, b in zip(left, right)]
        