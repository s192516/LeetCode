#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 672. Bulb Switcher II.py

n = 1
m = 1

n = 1
m = 2

n = 2
m = 1

n = 2
m = 2

n = 3
m = 1
#
#     m=1,  m=2,m=3,m=4
# n=1  2     2   2   2
# n=2  3     4   4   4
# n=3  4     7
# n=3下都是4  下都是7
#
# 还要考虑 m= 0的情况
class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        elif n == 1:
            return 2
        elif n ==2 and m == 1:
            return 3
        elif m== 1 or n == 2:
            return 4
        elif m == 2:
            return 7
        else:
            return 8




