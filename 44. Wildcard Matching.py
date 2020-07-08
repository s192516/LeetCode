#-*- coding:utf-8 -*-
#@Date   : 2018/12/9
#@Author : suyifan
#@File   : 44. Wildcard Matching.py



s = "abcb"
s = "abcd"
p = "*b"


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sp = 0
        pp = 0
        match = 0
        star = -1

        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == "?"):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == "*":
                star = pp
                pp += 1
                match = sp
            elif star != -1:
                # sp = match
                match += 1
                sp = match
                pp = star + 1
            else:
                return False

        # return True

        while pp < len(p) and p[pp] == "*":
            pp += 1

        return pp == len(p)

a = Solution()
q = a.isMatch(s,p)
print("q =",q)