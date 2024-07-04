class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)  # de-duplicate

        indegree = {c: 0 for word in words for c in word}

        # ["ab", "abc"] is valid, but ["abc", "ab"] is invalid in lexicographic order

        for first_word, second_word in pairwise(words):
            if len(second_word) < len(first_word) and first_word.startswith(second_word):
                return ""
            for a, b in zip(first_word, second_word):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break

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
