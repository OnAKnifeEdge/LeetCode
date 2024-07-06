class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = []
        tallest_building = 0
        for i in reversed(range(len(heights))):
            if heights[i] > tallest_building:
                tallest_building = heights[i]
                buildings.append(i)
        return buildings[::-1]
