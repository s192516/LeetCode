#-*- coding:utf-8 -*-
#@Date   : 2018/9/9
#@Author : suyifan
#@File   : 242. Valid Anagram.py

s = "sscat"
t = "catss"

# s = "rat"
# t = "cat"

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s = sorted(list(s))
        t = sorted(list(t))
        if s == t:
            return True
        else:
            return False




a = Solution()
q = a.isAnagram(s,t)
print("q=",q)