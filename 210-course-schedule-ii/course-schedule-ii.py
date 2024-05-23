class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = [[] for _ in range(numCourses)]
        for course, pre_course in prerequisites:
            d[pre_course].append(course)
        ingree = [0] * numCourses
        for course, _ in prerequisites:
            ingree[course] += 1

        start = [i for i, x in enumerate(ingree) if x == 0]

        q = deque(start)

        order = []
        while q:
            current = q.popleft()
            ingree[current] -= 1
            order.append(current)
            for nxt in d[current]:
                ingree[nxt] -= 1
                if ingree[nxt] == 0:
                    q.append(nxt)
        if len(order) != numCourses:
            return []
        return order
