class Solution:
    def permuteUnique_best(self, nums: List[int]) -> List[List[int]]:
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

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx):
            if idx == len(nums):
                result.append(nums[:])
                return

            lookup = set()
            for i in range(idx, len(nums)):
                if nums[i] in lookup:
                    continue
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
                lookup.add(nums[i])

        backtrack(0)
        return result
