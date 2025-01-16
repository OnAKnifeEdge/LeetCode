class Solution:
    # https://leetcode.com/problems/range-addition/ 370
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for booking in bookings:
            first, last, seats = booking[0] - 1, booking[1] - 1, booking[2]
            diff[first] += seats
            if last + 1 < n:
                diff[last + 1] -= seats
        s = 0
        for i, num in enumerate(diff):
            s += num
            diff[i] = s
        return diff
