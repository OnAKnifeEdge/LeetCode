class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_point = current_altitude = 0

        for g in gain:
            current_altitude += g
            highest_point = max(highest_point, current_altitude)
        
        return highest_point
        