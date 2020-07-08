#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 191. Number of 1 Bits.py

n = 111
n = 65
n = 11
n = 128
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        rtype = 0
        while n > 0:
            if n % 2 == 1:
                rtype += 1
            n //= 2
        return rtype

a = Solution()
q = a.hammingWeight(n)
print("q=",q)