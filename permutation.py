from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(current):
        # print(f'backtrack {current}')
        if current >= len(nums):
            # print('base case', current, nums)
            res.append(nums[:])

        for i in range(current, len(nums)):
            # print(f'swap for current={current}, i={i}, nums={nums}')
            nums[current], nums[i] = nums[i], nums[current]
            # print(f'===Start current={current}, i+1={i + 1}, nums={nums} ===')
            backtrack(current + 1)

            # print(f'===End current={current}, i+1={i + 1}, nums={nums} ===')
            nums[current], nums[i] = nums[i], nums[current]
            # print(f'swap back for current={current}, i={i}, nums={nums}')

        # print(f'end of backtrack {current}')

    backtrack(0)
    return res


nums = [1, 2, 3]
print(permute(nums))
