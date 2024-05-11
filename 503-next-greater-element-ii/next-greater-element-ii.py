class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []
        n = len(nums)

        for i in reversed(range(n * 2)):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if stack:
                result[i % n] = stack[-1]
            stack.append(nums[i % n])
        return result
