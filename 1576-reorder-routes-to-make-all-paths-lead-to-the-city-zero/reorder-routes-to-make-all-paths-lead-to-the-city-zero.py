class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        visited = {0}
        edges = set((a, b) for a, b in connections)
        changes = 0

        def dfs(city):
            nonlocal changes
            for neighbor in graph[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    changes += 1
                visited.add(neighbor)
                dfs(neighbor)
        dfs(0)
        return changes
