class Points(NamedTuple):
    first: int
    second: int


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [[Points(0, 0) for _ in range(n)] for _ in range(n)]
        # nums[i,...j] max points

        # Initialize the diagonal (base case: when the player picks the last number)
        for i in range(n):
            dp[i][i] = Points(first=nums[i], second=0)

        # 从下往上，从左往右
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                left = nums[i] + dp[i + 1][j].second
                right = nums[j] + dp[i][j - 1].second
                if left > right:
                    dp[i][j] = Points(left, dp[i + 1][j].first)

                else:
                    dp[i][j] = Points(right, dp[i][j - 1].first)

        point = dp[0][-1]
        return point.first >= point.second
