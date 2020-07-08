#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 172. Factorial Trailing Zeroes.py

n = 5
n = 100
#因为2的个数肯定比5多,所以考虑有多少个0只需要考虑有多少个5就好了
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
            count += n //5
            n //= 5
        return count


a = Solution()
q = a.trailingZeroes(n)
print("q=",q)