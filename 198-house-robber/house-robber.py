class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back, one_back = 0, 0
        for num in nums:
            one_back, two_back = max(two_back + num, one_back), one_back
        return one_back
        