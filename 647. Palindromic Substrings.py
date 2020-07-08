#-*- coding:utf-8 -*-
#@Date   : 2018/12/18
#@Author : suyifan
#@File   : 647. Palindromic Substrings.py

s = "aaaaa"
s = "aaa"
s = "abc"
s = "aba"


# https://blog.csdn.net/OneDeveloper/article/details/79853156
# 竟然跟这个不一样诶
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = n = len(s)

        map1 = [[False] * n for _ in range(n)]

        for i in range(n):
            map1[i][i] = True

        for i in range(1, n):
            if s[i] == s[i - 1]:
                map1[i - 1][i] = True
                num += 1

        for j in range(2, n):
            for i in range(n-1):

                if s[i] == s[j] and map1[i+1][j - 1]:
                    map1[i][j] = True
                    num += 1
        # print(map1)
        return num

a = Solution()
q = a.countSubstrings(s)
print("q =",q)