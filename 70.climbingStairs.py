#-*- coding:utf-8 -*-
#@Date   : 2018/9/4
#@Author : huali
#@File   : 70.climbingStairs.py

n =5

"""
1 1
2 2
3 1+2=3
4 2+3=5
5 3+5=8
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 2
        num1 = 1
        num2 = 2
        if n ==1:
            return 1
        if n == 2:
            return 2
        while count <n:
            num1,num2 = num2,num1+num2
            count += 1

        return num2

a = Solution()
q = a.climbStairs(n)
print("q=",q)