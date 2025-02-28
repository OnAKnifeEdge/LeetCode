class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(node, parent):
            total_time = 0
            for child in tree[node]:
                if child == parent:
                    continue
                child_time = dfs(child, node)
                if hasApple[child] or child_time:
                    total_time += 2 + child_time
            return total_time

        return dfs(0, -1)
