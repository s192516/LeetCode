#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 557. Reverse Words in a String III.py

s = "apple cat"

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1 = s.split()
        rtype = ""
        length = len(list1)
        for i in range(length):
            str_i = ""

            for j in range(len(list1[i])-1,-1,-1):
                str_i += list1[i][j]

            rtype +=" " + str_i
        return rtype.lstrip(" ")

a = Solution()
q = a.reverseWords(s)
print("q=",q)
