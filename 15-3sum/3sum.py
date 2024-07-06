class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()

        result = []

        def two_sum(idx):
            # find i, j so that nums[idx] + nums[i] + nums[j] == 0
            i = idx + 1
            j = n - 1
            while i < j:
                total = nums[idx] + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    result.append((nums[idx], nums[i], nums[j]))
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx == 0 or num != nums[idx - 1]:
                two_sum(idx)

        return result
