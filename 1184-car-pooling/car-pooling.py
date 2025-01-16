class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0] * 1001  # it represents all kilometers from 0 through 1000.

        for passengers, fr, to in trips:
            nums[fr] += passengers
            nums[to] -= passengers

        current_passengers = 0
        for num in nums:
            current_passengers += num
            if current_passengers > capacity:
                return False
        return True
