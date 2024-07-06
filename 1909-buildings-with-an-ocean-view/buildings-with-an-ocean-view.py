class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = []
        q = []
        for i in reversed(range(len(heights))):
            while q and q[-1] < heights[i]:
                q.pop()
            if not q:
                buildings.append(i)
            q.append(heights[i])
        buildings.reverse()
        return buildings
