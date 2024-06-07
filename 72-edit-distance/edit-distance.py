class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # base case 是 i 走完 s1 或 j 走完 s2，可以直接返回另一个字符串剩下的长度。
        # if s1[i] == s2[j]:
        #     啥都别做（skip）
        #     i, j 同时向前移动
        # else:
        # 三选一：
        #     插入（insert）
        #     删除（delete）
        #     替换（replace）

        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # dp[i][j] means min # of operations to convert word1[0..i) to word2[0..j)
        # 0 1 2 3 4 5
        # 1 w o r d 2
        # 2 o
        # 3 r
        # 4 d
        # 5 1
        for i in range(1, l1 + 1):
            dp[i][0] = i  # 第一列

        for j in range(1, l2 + 1):
            dp[0][j] = j  # 第一行

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert_case = dp[i - 1][j] + 1  # insert the same c to word1
                    delete_case = dp[i][j - 1] + 1  # delete the same c in word2
                    replace_case = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(insert_case, delete_case, replace_case)
        return dp[-1][-1]
