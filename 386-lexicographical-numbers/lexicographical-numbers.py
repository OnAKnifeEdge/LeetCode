class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(node):
            if node > n:
                return
            result.append(node)
            for i in range(0, 10):
                dfs(10 * node + i)

        for i in range(1, 10):
            dfs(i)
        return result
