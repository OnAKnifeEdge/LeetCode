class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) #dict a -> list of [b, value of a/b]

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        # a / b, a -> b
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q = deque()
            q.append((src, 1))
            visited = {src}

            while q:
                n, w = q.popleft() #node and weight
                if n == target:
                    return w
                for neighbor, weight in adj[n]:
                    if neighbor in visited:
                        continue
                    q.append((neighbor, w * weight))
                    visited.add(neighbor)
            return -1

        return [bfs(q[0], q[1]) for q in queries]