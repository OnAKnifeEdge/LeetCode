class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n - 1) + f(n - 2)
        one_step, two_step = 1, 1
        for i in range(2, n + 1):
            one_step, two_step = two_step, one_step + two_step
        return two_step
