class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            return False

        return dfs(source)
