class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for fr, to, cost in flights:
            graph[fr].append((to, cost))

        q = [(0, 0, src)]  # cost, stop, src]

        visited = {}  # src: stops

        while q:
            cost, stop, node = heappop(q)
            if node == dst and stop <= k + 1:
                return cost
            if node in visited and visited[node] < stop:
                continue
            visited[node] = stop
            neighbors = graph[node]
            for new_node, new_cost in neighbors:
                heappush(q, (cost + new_cost, stop + 1, new_node))
        return -1
