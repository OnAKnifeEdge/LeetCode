class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = [[] for _ in range(numCourses)]
        for course, pre_course in prerequisites:
            d[pre_course].append(course)

        visited = [0] * numCourses   # 0: unvisited, 1: visiting, 2: visited
        post_order = []

        def dfs(course):
            if visited[course] == 1:  # Cycle detected
                return True
            if visited[course] == 2:  # Already processed
                return False

            visited[course] = 1  # Mark as visiting

            for next_course in d[course]:
                if dfs(next_course):
                    return True

            visited[course] = 2  # Mark as processed
            post_order.append(course)
            return False

        for course in range(numCourses):
            if visited[course] == 0 and dfs(course):  # If cycle found, return []
                return []

        return post_order[::-1]
