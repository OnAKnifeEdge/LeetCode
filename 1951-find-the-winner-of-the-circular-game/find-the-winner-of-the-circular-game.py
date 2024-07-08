class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # f(n,k)=(f(n−1,k)+k) % n

        # def dfs(n, k):
        #     if n == 1:
        #         return 0
        #     return (dfs(n - 1, k) + k) % n

        # return dfs(n, k) + 1

        winner = 0

        for i in range(2, n + 1):
            winner = (winner + k) % i

        return winner + 1
