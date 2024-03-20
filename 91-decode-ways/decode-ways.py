class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # two_back = 1
        # one_back = 1

        # for i in range(1, len(s)):
        #     current = 0 # similar to dp[i]
        #     # If the one-digit substring is not '0' and we can consider the current digit as a single character.
        #     if s[i] != '0':
        #         current = one_back
        #     two_digit = int(s[i-1:i+1])
        #     if 10 <= two_digit <= 26:
        #         current += two_back
        #     two_back = one_back
        #     one_back = current

        # return one_back

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2: i])

            if one_digit != 0:
                dp[i] += dp[i - 1]
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
        