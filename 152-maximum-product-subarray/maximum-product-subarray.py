class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        cur_min, cur_max = 1, 1

        for num in nums:
            vals = (num, num * cur_min, num * cur_max)
            cur_max, cur_min = max(vals), min(vals)
            result = max(result, cur_max)
        return result


        