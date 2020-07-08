#-*- coding:utf-8 -*-
#@Date   : 2018/10/16
#@Author : suyifan
#@File   : 868. Binary Gap.py


N = 8

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 3:
            return 0

        count = 0
        max1 = 0
        begin = False
        while N:
            temp = N % 2

            if temp == 0 and begin:
                count += 1
                if count > max1:
                    max1 = count
            elif temp == 1 and N != 1:
                count = 1
                begin = True
            N //= 2

        if count > max1:
            max1 = count
        return max1

a = Solution()
q = a.binaryGap(N)
print("q =",q)