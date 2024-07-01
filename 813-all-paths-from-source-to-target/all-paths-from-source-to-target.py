class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        if not graph or not graph[0]:
            return paths
        n = len(graph)
        target = n - 1
        q = deque([[0]])

        while q:
            path = q.popleft()
            node = path[-1]
            for neighbor in graph[node]:
                new_path = path[:]
                new_path.append(neighbor)

                if neighbor == target:

                    paths.append(new_path)
                else:
                    q.append(new_path)
        return paths
