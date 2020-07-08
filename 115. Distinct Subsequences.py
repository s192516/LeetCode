#-*- coding:utf-8 -*-
#@Date   : 2018/12/31
#@Author : suyifan
#@File   : 115. Distinct Subsequences.py



s = "rabbbit"
t = "rabbit"

# s = "babgbag"
# t = "bag"

s = "ddd"
t = "dd"

class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        if not s:
            return 0
        len_s = len(s)
        len_t = len(t)
        dp = [[0 for i in range(len_s+1)] for j in range(len_t+1)]

        for i in range(len_s):
            if s[i] == t[0]:
                dp[0][i] = 1
        # for i in range(len_t):
        #     if t[i] == s[0]:
        #         dp[i][0] = 1


        for i in range(len_t):
            for j in range(len_s):
                if s[j] == t[i]:
                    dp[i+1][j+1] = dp[i][j]+dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        # for i in dp:
        #     print(i)
        return dp[len_t][len_s]
a = Solution()
q = a.numDistinct(s,t)
print("q =",q)