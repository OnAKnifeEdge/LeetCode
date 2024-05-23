class Solution:

    # Input: graph = [[1,2],[3],[3],[]]
    # Output: [[0,1,3],[0,2,3]]
    # Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last_node = len(graph) - 1
        result = []

        def backtrack(current_node, path):
            if current_node == last_node:
                result.append(path[:])
                result

            for next_node in graph[current_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        path = [0]
        backtrack(0, path)
        return result
