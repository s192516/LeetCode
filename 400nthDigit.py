#-*- coding:utf-8 -*-
#@Date   : 2018/8/31
#@Author : huali
#@File   : 400nthDigit.py


n =111
s=""
for i in range(1,n+1):
    s +=str(i)
print(s)
print(len(s))
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
