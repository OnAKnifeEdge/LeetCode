class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        dp(dst, k) = min(
                        dp(s1, k - 1) + w1,
                        dp(s2, k - 1) + w2
                    )
        """

        indegree = defaultdict(list)
        for f, t, price in flights:
            indegree[t].append((f, price))

        @cache
        def dp(destination, i):
            if destination == src:
                return 0
            if i == 0:
                return -1

            if destination not in indegree:
                return -1

            result = float("inf")
            for f, price in indegree[destination]:
                sub_probelm = dp(f, i - 1)
                if sub_probelm != -1:
                    result = min(result, sub_probelm + price)
            return result if result != float("inf") else -1

        result = dp(dst, k + 1)
        return result
