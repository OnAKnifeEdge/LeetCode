class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) == 0 or r * c != len(nums) * len(nums[0]):
            return nums

        reshaped = []  # Initialize the reshaped matrix
        temp = []

        for row in nums:
            for val in row:
                temp.append(val)
                if len(temp) == c:
                    reshaped.append(temp)
                    temp = []
        return reshaped