class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        points = defaultdict(int)
        for num in nums:
            points[num] += num

        # dp[i] = max(dp[i-1], dp[i-2] + points[nums[i]])

        # dp[0] = 0
        # dp[1] = points[numbers[0]]

        numbers = sorted(points.keys())
        a, b = 0, points[numbers[0]]

        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i - 1] + 1:
                a, b = b, max(b, a + points[numbers[i]])
            else:
                a, b = b, b + points[numbers[i]]

        return b
