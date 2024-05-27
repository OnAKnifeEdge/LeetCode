class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        # build the graph
        for city1, city2, cost in connections:
            graph[city1].append((cost, city2))
            graph[city2].append((cost, city1))

        # priority queue
        queue = [(0, 1)]  # (cost, city)

        # set to keep track of visited cities
        visited = set()

        totalCost = 0
        while queue:
            cost, city = heappop(queue)
            if city not in visited:
                visited.add(city)
                totalCost += cost

                for nextCost, nextCity in graph[city]:
                    heappush(queue, (nextCost, nextCity))

        # check if all cities are visited
        return totalCost if len(visited) == n else -1
