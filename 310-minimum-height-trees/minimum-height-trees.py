class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # https://claude.ai/chat/38b6d74b-7744-4175-8cae-d64878f22aa8
        if n <= 2:
            return list(range(n))

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque([i for i in range(n) if len(graph[i]) == 1])

        remaining_nodes = n

        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
                # del graph[leaf]  # Remove the leaf node from the graph

        return list(leaves)
