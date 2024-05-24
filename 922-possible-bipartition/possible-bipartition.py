class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        d = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            d[a].append(b)
            d[b].append(a)

        color = [0] * (n + 1)

        def dfs(node, c):
            color[node] = c
            for neighbor in d[node]:
                if color[neighbor] == c:
                    return True  # has same color
                if color[neighbor] == 0 and dfs(neighbor, -c):
                    return True  # has different color but contains same color
            return False

        for i in range(1, n + 1):
            if color[i] == 0 and dfs(i, 1):
                return False
        return True
