class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, delay in times:
            graph[src].append((delay, dst))
        q = [(0, k)]
        visited = set()
        time = 0

        while q:
            delay, node = heappop(q)
            if node in visited:
                continue
            visited.add(node)
            time = max(time, delay)

            neighbors = graph[node]

            for new_delay, new_node in neighbors:
                if new_node in visited:
                    continue
                heappush(q, (delay + new_delay, new_node))
        return time if len(visited) == n else -1
