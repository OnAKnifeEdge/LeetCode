class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)  # de-duplicate

        indegree = {c: 0 for word in words for c in word}

        for first_word, second_word in pairwise(words):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        indegree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""  # Invalid order, return ""

        order = []
        q = deque([c for c, v in indegree.items() if v == 0])
        while q:
            c = q.popleft()
            order.append(c)
            for d in graph[c]:
                indegree[d] -= 1
                if indegree[d] == 0:
                    q.append(d)

        if len(order) == len(indegree):
            return "".join(order)

        return ""
