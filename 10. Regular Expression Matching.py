#-*- coding:utf-8 -*-
#@Date   : 2018/11/30
#@Author : suyifan
#@File   : 10. Regular Expression Matching.py

s = "aa"
p = "a*"

# s = "a"
# s = "abca"
# p = "a*.a"
#
# s = "abca"
# p = "a.*a"
#
# s = "aaa"
# p = "aaaa*"

s = "aab"
p = "c*a*b"
s = ""
p = "." # False
#
s = ""
p = ".*" # True
# s = ""
# p = "**"
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # if not s and not p:
        #     return True
        # if not s or not p:
        #     return False

        len_p = len(p)
        len_s = len(s)
        dp = [[False]*(len_p+1) for _ in range(len_s+1)]
        dp[0][0] = True
        for i,char in enumerate(p):
            if char == "*" :#and dp[0][i-1]:
                dp[0][i+1] = True

        for i in range(len_s):
            for j in range(len_p):
                if p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                if p[j]==".":
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == "*":
                    if p[j-1] != s[i] and p[j-1] != ".":
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]

        return dp[-1][-1]

a = Solution()
q = a.isMatch(s,p)
print("q =",q)
