class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        subtree_sizes = [0] * n
        tree = defaultdict(list)  # parent: children
        for child, parent in enumerate(parents):
            if parent != -1:  # Skip the root node with parent -1
                tree[parent].append(child)

        def dfs(node) -> int:
            size = 1
            for child in tree[node]:
                size += dfs(child)
            subtree_sizes[node] = size
            return size

        dfs(0)

        max_score = 0
        count = 0

        for node in range(n):
            score = 1
            for child in tree[node]:
                score *= subtree_sizes[child]

            # If the node is not root, multiply by the size of the remaining subtree.
            if node != 0:
                remaining_tree_size = n - subtree_sizes[node]
                score *= remaining_tree_size

            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1

        return count
