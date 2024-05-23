class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = [[] for _ in range(numCourses)]
        for course, pre_course in prerequisites:
            d[pre_course].append(course)

        visited = [False] * numCourses
        exploring = [False] * numCourses
        post_order = []

        def dfs(course):
            if exploring[course]:
                return True

            if visited[course]:
                return False
            visited[course] = True
            exploring[course] = True

            for next_course in d[course]:
                if dfs(next_course):
                    return True
            post_order.append(course)
            exploring[course] = False
            return False

        for course in range(numCourses):
            if not visited[course] and dfs(course):
                return []

        return post_order[::-1]
