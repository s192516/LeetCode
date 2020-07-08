#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 231. Power of Two.py

n = 32

#考虑 n = 0
#负数直接返回false
# n & (n-1) == 0可以直接计算结果

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rtype = True

        if n < 1:
            return False
        while n > 1:
            if n % 2 ==0:
                n /=2
            else:
                rtype = False
                break
        return rtype
        # return (n & (n - 1)) == 0

a = Solution()
q = a.isPowerOfTwo(n)
print("q=",q)