class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        

    def helper(self, nums: List[int]) -> int:
        two_back, one_back = 0, 0 
        for num in nums:
            one_back, two_back = max(two_back + num, one_back), one_back
        return one_back