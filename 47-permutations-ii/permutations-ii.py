class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        used = [False] * len(nums)

        def permute(current: List[int]):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                # only when duplicate and prev one has been used
                current.append(nums[i])
                used[i] = True
                permute(current)
                current.pop()
                used[i] = False

        permute([])
        return result
