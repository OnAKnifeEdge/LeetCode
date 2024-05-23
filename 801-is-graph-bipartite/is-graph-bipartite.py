class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        # 0 means not colored, 1, -1 means different colors
        color = [0] * n

        # if has same color True
        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return True
                if color[neighbor] == 0 and dfs(neighbor, -c):
                    return True
            return False

        for i in range(n):
            if color[i] == 0 and dfs(i, 1):
                return False
        return True
