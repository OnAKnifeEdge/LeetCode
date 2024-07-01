class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
        if even > 1:
            return True
        return False
