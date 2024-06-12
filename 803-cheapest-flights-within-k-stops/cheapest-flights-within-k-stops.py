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

        visited = {}

        graph = defaultdict(list)
        for f, t, price in flights:
            graph[f].append((t, price))

        min_heap = [(0, 0, src)]  # cost, stops, node
        while min_heap:
            cost, stops, node = heappop(min_heap)
            if node == dst and stops <= k + 1:
                return cost
            if node in visited and visited[node] < stops:
                continue  # Skip if we visited the node with fewer stops
            visited[node] = stops
            for next_node, next_cost in graph[node]:
                heappush(min_heap, (next_cost + cost, stops + 1, next_node))
        return -1
