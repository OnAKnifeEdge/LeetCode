class Solution:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {i: WHITE for i in range(n)}
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        def dfs(node):
            if color[node] == GRAY:
                return False
            if color[node] == BLACK:
                return True
            if not graph[node] and node != destination:
                return False
            color[node] = GRAY
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            color[node] = BLACK
            return True

        return dfs(source)
