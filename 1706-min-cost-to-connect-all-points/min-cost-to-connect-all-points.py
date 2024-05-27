class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        n = len(points)

        total_cost = 0
        visited = set()

        queue = [(0, 0)]  # (distance, vertex)

        while len(visited) < n:
            d, u = heappop(queue)
            if u not in visited:
                visited.add(u)
                total_cost += d
                for v in range(n):
                    if v not in visited:
                        d = manhattan(points[u], points[v])
                        heappush(queue, (d, v))
        return total_cost
