#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 829. Consecutive Numbers Sum.py

#如果n能表示为2个数相加之和,那么这两个数必然一奇一偶,这两个相邻的数必然除2余1
#如果n能表示为3革数相加之和,那么这三个数必然为3的倍数
#相邻的k个数之和除n的余数为Sk % k
#如果n能表示为k个数之和,那么他必然和 Sk % k同余

n = 1
n = 9
n = 5
# n = 15
# n =123



class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        rtype = 0
        i = 2
        q = 1
        while q < N:
            q = i * (i + 1) / 2

            if (n % i) == (q % i):
                rtype += 1
            i += 1
        return rtype+1

a = Solution()
q = a.consecutiveNumbersSum(n)
print("q=",q)