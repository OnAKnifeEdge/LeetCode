class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        # 0 means not colored, 1, -1 means different colors
        color = [0] * n

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
                if color[neighbor] == 0 and not dfs(neighbor, -c):
                    return False
            return True

        for i in range(n):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True
