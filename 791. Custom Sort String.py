#-*- coding:utf-8 -*-
#@Date   : 2018/12/18
#@Author : suyifan
#@File   : 791. Custom Sort String.py

S = "cba"
T = "abcd"

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # s_dict = {}
        t_dict = {}
        # for i,c in enumerate(S):
        # s_dict[c] = i
        s_set = set(S)
        ans = ""
        for c in T:
            if c not in s_set:
                ans += c
            else:
                t_dict[c] = t_dict.get(c,0) + 1

        # ans = ""
        for c in S:
            ans += c * t_dict.get(c,0)

        return ans

a = Solution()
q = a.customSortString(S,T)
print("q =",q)