class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        if not isConnected:
            return 0

        n = len(isConnected)

        for i, j in itertools.combinations(range(n), 2):
            if isConnected[i][j] == 0:
                continue
            graph[i].append(j)
            graph[j].append(i)

        visited = set()

        def dfs(u):
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    dfs(v)

        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)

        return count
