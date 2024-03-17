class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        @cache
        def dp(num): 
            # dp(i) is the max points when reach to num i
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            
            return max(dp(num - 1), dp(num - 2) + points[num])
        
        return dp(max_number)



        