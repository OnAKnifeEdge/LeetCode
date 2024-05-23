class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        d = [[] for _ in range(numCourses)]
        for course, pre_course in prerequisites:
           d[course].append(pre_course)

        visited = [False] * numCourses
        exploring = [False] * numCourses

        def traverse(course):
            if exploring[course]:
                return True
            if visited[course]:
                return False
            visited[course] = True
            exploring[course] = True
            for pre_course in d[course]:
                if traverse(pre_course):
                    return True
            exploring[course] = False
            return False

        for course in range(numCourses):
            if traverse(course):
                return False
        return True

        