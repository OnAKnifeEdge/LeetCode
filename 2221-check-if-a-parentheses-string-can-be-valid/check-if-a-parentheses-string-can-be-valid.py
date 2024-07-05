class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        def check(s: str, locked: str, c: str) -> bool:
            balance = 0
            for i in range(len(s)):
                if locked[i] == "0" or s[i] == c:
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return True

        if not check(s, locked, "("):
            print("( >= )")
            return False

        if not check(s[::-1], locked[::-1], ")"):
            print(") >= (")
            return False

        return True
