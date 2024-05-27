class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        graph = defaultdict(list)

        for (a, b), p in zip(edges, succProb):
            graph[a].append((p, b))
            graph[b].append((p, a))

        q = [(-1, start)]
        probabilities = [0] * n
        probabilities[start] = 1
        while q:
            p, node = heappop(q)
            p *= -1
            if node == end:
                return p
            for new_p, new_node in graph[node]:
                probability = new_p * probabilities[node]
                if probability > probabilities[new_node]:
                    probabilities[new_node] = probability
                    heappush(q, (-probability, new_node))
        return 0
