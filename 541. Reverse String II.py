#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 541. Reverse String II.py

s = "abcdefg"
k = 2
s = "abcdefg"
k = 1
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        rtype = ""
        while i + 2 * k - 1 <= j:
            for q in range(i + k - 1, i-1, -1):
                rtype += s[q]
            i += k
            rtype += s[i:i + k]
            i += k
        if i + k > j:
            for q in range(j, i - 1, -1):
                rtype += s[q]
            # return rtype

        if i + k <= j:
            for q in range(i + k - 1, i - 1, -1):
                rtype += s[q]
            i += k
            rtype += s[i:]
            # return rtype
        return rtype

a = Solution()
q = a.reverseStr(s,k)
print("q = ",q)

#q =  abcbadedcbaf