class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        water = numBottles
        while numBottles >= numExchange:
            newBottles, remaining = divmod(numBottles, numExchange)
            water += newBottles
            numBottles = newBottles + remaining
        return water
