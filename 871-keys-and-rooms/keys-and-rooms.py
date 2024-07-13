class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        q = deque([0])
        while q:
            idx = q.popleft()
            visited.add(idx)
            for key in rooms[idx]:
                if key not in visited:
                    q.append(key)
        return len(visited) == n
