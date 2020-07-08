#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 326. Power of Three.py

n = 27

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rtype = True

        if n < 1:
            return False
        while n > 1:
            if n % 3 == 0:
                n /= 3
            else:
                rtype = False
                break
        return rtype

a = Solution()
q = a.isPowerOfThree(n)
print("q=",q)