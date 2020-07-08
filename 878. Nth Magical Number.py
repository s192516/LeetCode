#-*- coding:utf-8 -*-
#@Date   : 2019/1/11
#@Author : suyifan
#@File   : 878. Nth Magical Number.py

N,A,B = 2 ,99,66
N,A,B = 1,2,3
N,A,B = 4,2,3
N,A,B = 7,5,8 # ans=24
N,A,B = 1000000000,40000,40000
class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        min1 = self.beishu(A, B)
        aa = min1 // A
        bb = min1 // B
        z = aa + bb - 1
        m = N // z
        n = N % z
        ans = min1 * m
        if n == 0:
            return ans % (10**9+7)
        # print(min1)
        min_q,a = 0,min(A,B)
        max_q = b = max(A,B)
        # min_q,max_q = A,B
        ans1 = 0
        for i in range(n):

            if min_q + a < max_q:
                min_q += a
                ans1 = min_q
            elif min_q + a == max_q:
                ans1 = max_q
                min_q += a
                max_q += b
            else:
                # min_q = B
                ans1 = max_q
                max_q += b

        print(ans,ans1)
        return (ans+ans1) % (10**9 + 7)

    def beishu(self, A, B):
        import math
        min1 = min(A, B)
        max1 = max(A, B)
        if max1 % min1 == 0:
            return max1

        ans = 1
        while min1 % 2 == 0 and max1 % 2 == 0:
            min1 //= 2
            max1 //= 2
            ans *= 2

        n = min1+1
        q = int(math.sqrt(min1)) + 1
        for i in range(3, n, 2):
            while min1 % i == 0 and max1 % i == 0:
                ans *= i
                min1 //= i
                max1 //= i
            if min1 < i:
                break
        return ans * min1 * max1

a = Solution()
q = a.nthMagicalNumber(N,A,B)
print("q =",q)