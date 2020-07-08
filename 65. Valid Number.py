#-*- coding:utf-8 -*-
#@Date   : 2018/12/7
#@Author : suyifan
#@File   : 65. Valid Number.py

s = "123"

s = "1e1.2"
s = "-1."
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        num_seen = False
        num_fater_e = True
        point_seen = False
        e_seen = False


        n = len(s)
        for i in range(n):
            if s[i].isdigit():
                num_seen = True
                num_fater_e = True
            elif s[i] == ".":
                if e_seen or point_seen:
                    return False
                point_seen = True
            elif s[i] == "e":
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_fater_e = False
            elif s[i] == "+" or s[i] == "-":
                if i != 0 and s[i-1] != "e":
                    return False
            else:
                return False

        return num_seen and num_fater_e

a = Solution()
q = a.isNumber(s)
print("q =",q)