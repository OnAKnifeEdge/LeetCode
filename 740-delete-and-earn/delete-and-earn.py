class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        # top down recurrence
        # @cache
        # def dp(num): 
        #     # dp(i) is the max points when reach to num i
        #     if num == 0:
        #         return 0
        #     if num == 1:
        #         return points[1]
            
        #     return max(dp(num - 1), dp(num - 2) + points[num])
        
        # return dp(max_number)
        # bottom up case

        # dp = [0] * (max_number + 1)
        # dp[1] = points[1]

        # for i in range(2, max_number + 1):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
        # return dp[max_number]

        # space optimazation

        # two = 0
        # one = points[1]
        # for i in range(2, max_number + 1):
        #     two, one = one, max(one, two + points[i])
        # return one


        # optimization with sorting
        elements = sorted(points.keys())
        if not elements:
            return 0
        two = 0
        one = points[elements[0]]
        # loop elements
        for i in range(1, len(elements)):
            current = elements[i]
            if current == elements[i - 1] + 1:
                two, one = one, max(one, two + points[current])
            else:
                two, one = one, one + points[current]
        return one




        