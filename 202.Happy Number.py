#-*- coding:utf-8 -*-
#@Date   : 2018/9/8
#@Author : suyifan
#@File   : 202.Happy Number.py

n =19

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        dict1 = {}
        n = str(n)

        while True:
            sum = 0
            for i in range(len(n)):
                sum += int(n[i])**2

            if sum == 1:
                return True

            if sum in dict1:
                return False
            else :
                dict1[sum] = 1

            n = str(sum)

a = Solution()
q = a.isHappy(n)
print("q= ",q)
