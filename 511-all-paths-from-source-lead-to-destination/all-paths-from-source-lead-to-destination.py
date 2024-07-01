class Solution:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        color = {i: "white" for i in range(n)}
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        def dfs(node):
            if color[node] == "gray":
                return False
            if color[node] == "black":
                return True
            if not graph[node] and node != destination:
                # Terminal node and NOT the destination
                return False
            color[node] = "gray"
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            color[node] = "black"
            return True

        return dfs(source)
