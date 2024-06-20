class Solution:
    def rob(self, nums: List[int]) -> int:
        one_back, two_back = 0, 0

        for num in nums:
            one_back, two_back = max(one_back, two_back + num), one_back
        return one_back
