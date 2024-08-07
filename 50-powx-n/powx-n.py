class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n < 0: return 1 / pow(x, -n)
        # x ** n = 1/ (x ** -n)

        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        result = 1

        while n != 0:
            if n % 2 == 1:
                result *= x
                n -= 1

            x *= x
            n //= 2

        return result
