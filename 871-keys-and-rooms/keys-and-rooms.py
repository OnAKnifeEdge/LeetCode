class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        s = [0]

        while s:
            node = s.pop()
            for key in rooms[node]:
                if not seen[key]:
                    seen[key] = True
                    s.append(key)

        return all(seen)
        