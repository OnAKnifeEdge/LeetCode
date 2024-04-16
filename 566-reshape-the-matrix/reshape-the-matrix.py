class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        # if len(nums) == 0 or r * c != len(nums) * len(nums[0]):
        #     return nums

        # reshaped = []  # Initialize the reshaped matrix
        # temp = []

        # for row in nums:
        #     for val in row:
        #         temp.append(val)
        #         if len(temp) == c:
        #             reshaped.append(temp)
        #             temp = []
        # return reshaped

        if len(nums) == 0 or r * c != len(nums) * len(nums[0]):
            return nums

        rows, cols = len(nums), len(nums[0])  # The dimensions of the original matrix

        reshaped = [[0] * c for _ in range(r)]
        cnt = 0  
        
        for i in range(rows):
            for j in range(cols):
                ii, jj = divmod(cnt, c)
                reshaped[ii][jj] = nums[i][j]  
                cnt += 1  
                
        return reshaped