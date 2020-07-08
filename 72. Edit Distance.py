#-*- coding:utf-8 -*-
#@Date   : 2018/12/31
#@Author : suyifan
#@File   : 72. Edit Distance.py

word1 = "rabbit"
word2 = "rabbbit"

word1 = "a"
word2 = "b"

word1 = "intention"
word2 = "execution"

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        dp = [[0 for i in range(m+1)]for j in range(n+1)]
        # print(dp)
        for i in range(m+1):
            dp[0][i] = i
        for j in range(n+1):
            dp[j][0] = j

        for j in range(m):
            for i in range(n):
                if word1[j] == word2[i]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1])+1
        # print(dp)
        # for i in dp:
        #     print(i)
        return dp[n][m]


a = Solution()
q = a.minDistance(word1,word2)
print("q =",q)