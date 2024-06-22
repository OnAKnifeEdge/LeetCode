class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        used = [False] * n

        def backtrack(current):
            if len(current) == n:
                result.append(current[:])
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                # 当出现重复元素时，
                # 比如输入 nums = [1,2,2',2'']，
                # 2' 只有在 2 已经被使用的情况下才会被选择，
                # 同理，2'' 只有在 2' 已经被使用的情况下才会被选择，
                # 这就保证了相同元素在排列中的相对位置保证固定。
                # skip duplicates where the previous identical element wasn't used.
                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue
                current.append(num)
                used[i] = True
                backtrack(current)
                current.pop()
                used[i] = False

        backtrack([])
        return result
