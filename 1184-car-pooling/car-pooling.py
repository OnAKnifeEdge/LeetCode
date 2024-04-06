class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0] * 1001  # it represents all kilometers from 0 through 1000.

        for trip in trips:
            passengers, start, end = trip
            nums[start] += passengers  # Pick up passengers
            nums[end] -= passengers    # Drop off passengers

        # Use prefix sum method to calculate the number of passengers at each kilometer
        current_passengers = 0
        for num in nums:
            current_passengers += num
            
            # If at any point the number of passengers in the car exceeds its capacity, return False
            if current_passengers > capacity:
                return False

        # If the loop completes without returning False, then the trips are possible within capacity
        return True