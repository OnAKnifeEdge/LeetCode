class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #  dp[i][j] represents whether the substring s3[:i+j] can be formed by interleaving s1[:i] and s2[:j].
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        # row is s1, col is s2
        dp = [[False] * (l1 + 1) for _ in range(l2 + 1)]
        
        # base case
        dp[0][0] = True

        for i in range(1, 1 + l1):
            # 第一行
            dp[0][i] = dp[0][i - 1] and s1[i - 1] == s3[i - 1]

        for i in range(1, 1 + l2):
            # 第一列
            dp[i][0] = dp[i - 1][0] and s2[i - 1] == s3[i - 1]

        for i in range(1, 1 + l2):
            for j in range(1, 1 + l1):
                one = dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]
                two = dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]
                dp[i][j] = one or two

        return dp[l2][l1]
               


        