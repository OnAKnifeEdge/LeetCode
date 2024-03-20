class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))



    def rob_simple(self, nums: List[int]) -> int:
        two_back = 0
        one_back = 0
        for num in nums:
            two_back, one_back = one_back, max(two_back + num, one_back)
        return one_back
        # t1 = 0
        # t2 = 0
        # for num in nums:
        #     # t1, t2 = max(num + t2, t1), t1
        #     temp = t1
        #     t1 = max(num + t2, t1)
        #     t2 = temp
        # return t1