class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)
        for idx, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(idx)

        n = len(parents)
        sizes = [0] * n # sizes of subtree containing the node itself

        def dfs(node): # return the size
            total = 0
            for child in tree[node]:
                total += dfs(child)
            sizes[node] = total + 1
            return sizes[node]

        dfs(0)

        highest_score = 0
        count = 0

        for node in range(n):
            score = 1
            for child in tree[node]:
                score *= sizes[child]
            upper_tree_cnt = n - sizes[node]
            if upper_tree_cnt > 0:
                score *= upper_tree_cnt
            if score > highest_score:
                highest_score = score
                count = 1
            elif score == highest_score:
                count += 1
        return count


