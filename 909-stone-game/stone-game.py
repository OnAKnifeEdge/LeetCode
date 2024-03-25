class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            even = bool((r - l) % 2)
            if even:
                dp[(l, r)] = max(piles[l] + dfs(l + 1, r), piles[r] + dfs(l, r - 1))
            else:
                dp[(l, r)] = min(dfs(l + 1, r) - piles[l], dfs(l, r - 1) - piles[r])
            return dp[(l, r)]

        return dfs(0, len(piles) - 1)
