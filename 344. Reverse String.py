#-*- coding:utf-8 -*-
#@Date   : 2018/9/9
#@Author : suyifan
#@File   : 344. Reverse String.py

s= "sdf"
# s= ""

# class Solution:
#     def reverseString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         i = 0
#         j = len(s) - 1
#         s = list(s)
#         while i < j:
#             s[i],s[j] = s[j],s[i]
#             i += 1
#             j -= 1
#         rtype = ""
#         for i in s:
#             rtype += i
#         return rtype

#

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s = list(s)
        rtype = ""

        while i < j:
            rtype += s[j]
            s[j] = s[i]
            i += 1
            j -= 1

        for i in range(j,-1,-1):
            rtype += s[i]
        return rtype



a = Solution()
q = a.reverseString(s)
print("q=",q)