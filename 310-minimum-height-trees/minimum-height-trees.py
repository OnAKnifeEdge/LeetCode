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

        while len(graph) > 2:
            for _ in range(len(leaves)):
                # remove the leaf from the leaves
                leaf = leaves.popleft()

                # remove the leaf from graph
                neighbor = graph[leaf].pop()
                del graph[leaf]

                # remove leaf from neighbor dependency
                graph[neighbor].remove(leaf)

                # if neighbor is leaf
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(graph.keys())
