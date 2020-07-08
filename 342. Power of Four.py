#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 342. Power of Four.py

num = 32

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        rtype = True

        if num < 1:
            return False
        while num > 1:
            if num % 4 == 0:
                num /= 4
            else:
                rtype = False
                break
        return rtype

a = Solution()
q = a.isPowerOfFour(num)
print ("q=",q)