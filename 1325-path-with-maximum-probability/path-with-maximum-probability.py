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
        for (x, y), probability in zip(edges, succProb):
            graph[x].append((probability, y))
            graph[y].append((probability, x))

        max_heap = [(-1, start)]  # max_probability so far and the current node
        probabilities = [0] * n
        probabilities[start] = 1

        while max_heap:
            p, node = heappop(max_heap)

            if node == end:
                return -p

            for new_p, new_node in graph[node]:
                probability = probabilities[node] * new_p
                if probability <= probabilities[new_node]:
                    continue
                heappush(max_heap, (-probability, new_node))
                probabilities[new_node] = probability
        return 0
