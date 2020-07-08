#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 190. Reverse Bits.py



n = 15
n = 17
n = 6
n = 96
# n = 43261596
# 0000-0010-1001-0100-0001-1110-1001-1100
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # int1 = 0
        if n % 2 == 0:
            int1 = 1
        else:
            int1 = 0
        while n > 0 :
            int2 = n % 2
            int1 = int2  + int1 * 2
            n //= 2
        print("int1",int1)
        i = 0
        int4 = 0

        while i < 31:
            int3 = int1 % 2
            int4 = int3 + int4 *2
            int1 //= 2
            i += 1


        return int4

a = Solution()
q = a.reverseBits(n)
print("q=",q)