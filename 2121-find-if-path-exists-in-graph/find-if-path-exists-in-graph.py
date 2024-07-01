class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = {source}
        q = deque([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                q.append(neighbor)

        return False
