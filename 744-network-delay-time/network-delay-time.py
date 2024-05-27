class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, delay in times:
            graph[src].append((delay, dst))

        q = [(0, k)]
        visited = set()
        time = 0

        while q:
            delay, dst = heappop(q)

            if dst in visited:
                continue

            visited.add(dst)

            time = max(time, delay)

            neighbors = graph[dst]

            for new_delay, new_dst in neighbors:
                if new_dst in visited:
                    continue

                heappush(q, (delay + new_delay, new_dst))

        return time if len(visited) == n else -1
