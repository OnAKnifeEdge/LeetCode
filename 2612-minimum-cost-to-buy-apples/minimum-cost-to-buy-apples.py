class Solution:
    def minCost(
        self, n: int, roads: List[List[int]], appleCost: List[int], k: int
    ) -> List[int]:
        graph = defaultdict(list)
        for a, b, cost in roads:
            graph[a - 1].append((cost, b - 1))
            graph[b - 1].append((cost, a - 1))

        result = list(appleCost)
        q = [(price, i) for i, price in enumerate(appleCost)]

        while q:
            cost, current_city = heappop(q)
            if cost > appleCost[current_city]:
                continue
            for new_cost, new_city in graph[current_city]:
                c = cost + new_cost * (k + 1)
                if c < result[new_city]:
                    result[new_city] = c
                    heappush(q, (c, new_city))
        return result
