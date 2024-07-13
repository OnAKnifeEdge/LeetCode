class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = {0}

        q = deque([0])
        while q:
            idx = q.popleft()
            keys = rooms[idx]
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return len(visited) == n
