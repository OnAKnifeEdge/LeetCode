class Solution:
    def permute_swap(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx: int):
            if idx == len(nums):
                result.append(nums[:])
                return

            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        backtrack(0)

        return result

    def permute_backtrack(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current: List[int]):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for num in nums:
                if num in current:
                    continue
                current.append(num)
                backtrack(current)
                current.pop()

        backtrack([])

        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def backtrack(current: List[int]):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i, num in enumerate(nums):
                if used[i]:
                    continue
                current.append(num)
                used[i] = True
                backtrack(current)
                current.pop()
                used[i] = False

        backtrack([])
        return result
