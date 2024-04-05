class Solution:
    # def productExceptSelf1(self, nums: List[int]) -> List[int]:
    #     left = [1] * len(nums)
    #     for i in range(1, len(nums)):
    #         left[i] = nums[i - 1] * left[i - 1]
    #         # 1， 1， 2， 6
    #     right = [1] * len(nums)
    #     for j in range(len(nums) - 2, -1, -1):
    #         right[j] = nums[j + 1] * right[j + 1]
    #         # 24，12，4，1
    #     return [a * b for a, b in zip(left, right)]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        prefix = suffix = 1

        # [1, 2, 3, 4]

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            # [1, 1, 2, 6]
        
        for i in reversed(range(n)):
            answer[i] *= suffix
            #postfix= [1, 4, 12, 24]
            suffix *= nums[i]
        
        return answer