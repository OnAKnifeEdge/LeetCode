class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        d = [[] for _ in range(numCourses)]
        for course, pre_course in prerequisites:
            d[pre_course].append(course)
        ingree = [0] * numCourses
        for course, _ in prerequisites:
            ingree[course] += 1

        start = [i for i, x in enumerate(ingree) if x == 0]

        q = deque(start)

        count = 0

        while q:
            current = q.popleft()
            ingree[current] -= 1
            count += 1
            for nxt in d[current]:
                ingree[nxt] -= 1
                if ingree[nxt] == 0:
                    q.append(nxt)

        return count == numCourses


    # def canFinish_dfs_loop(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     d = [[] for _ in range(numCourses)]
    #     for course, pre_course in prerequisites:
    #         d[course].append(pre_course)

    #     visited = [False] * numCourses
    #     path = []
    #     loops = set()

    #     def find_loop(course):
    #         visited[course] = True
    #         path.append(course)
    #         for pre_course in d[course]:
    #             if pre_course in path:  # detected
    #                 idx = path.index(pre_course)
    #                 loops.add(tuple(path[idx:]))
    #             elif not visited[pre_course]:
    #                 find_loop(pre_course)
    #         path.pop()

    #     for course in range(numCourses):
    #         if not visited[course]:
    #             find_loop(course)
        
    #     if loops:
    #         return False
    #     return True


    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        d = [[] for _ in range(numCourses)]
        for course, pre_course in prerequisites:
            d[course].append(pre_course)

        visited = [False] * numCourses
        exploring = [False] * numCourses

        def is_cyclic(course):
            if exploring[course]:
                return True
            if visited[course]:
                return False
            visited[course] = True
            exploring[course] = True
            for pre_course in d[course]:
                if is_cyclic(pre_course):
                    return True
            exploring[course] = False
            return False

        for course in range(numCourses):
            if is_cyclic(course):
                return False
        return True
