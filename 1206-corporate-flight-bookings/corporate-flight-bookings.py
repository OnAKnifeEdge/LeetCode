class Solution:
    # https://leetcode.com/problems/range-addition/ 370
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        
        for booking in bookings:
            i, j, val = booking[0] - 1, booking[1] - 1, booking[2]
            diff[i] += val
            if j + 1 < n:
                diff[j + 1] -= val

        s = 0
        for idx, num in enumerate(diff):
            s += num
            diff[idx] = s
        return diff
        