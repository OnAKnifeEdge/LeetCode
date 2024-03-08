class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        s = [0]

        while s:
            room = s.pop()
            seen.add(room)
            for key in rooms[room]:
                if key not in seen:
                    s.append(key)

        return len(seen) == len(rooms)
        