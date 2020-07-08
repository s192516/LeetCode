#-*- coding:utf-8 -*-
#@Date   : 2018/9/8
#@Author : suyifan
#@File   : 205. Isomorphic Strings.py

s = "ed d"
t = "dt,t"
s = "ab"
t = "aa"
s = "ab"
t = "ca"
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}

        for i in range(len(s)) :
            if s[i] in dict1:
                if dict1[s[i]] == t[i]:
                    pass
                else :
                    return False
            else :
                dict1[s[i]] = t[i]
        # print(dict1)
        dict1 = {}
        for i in range(len(t)) :
            if t[i] in dict1:
                if dict1[t[i]] == s[i]:
                    pass
                else :
                    return False
            else :
                dict1[t[i]] = s[i]

        return True

a = Solution()
q = a.isIsomorphic(s,t)
print("q=",q)