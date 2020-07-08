#-*- coding:utf-8 -*-
#@Date   : 2019/1/2
#@Author : suyifan
#@File   : 793. Preimage Size of Factorial Zeroes Function.py


# K = 1
# K = 5
class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """

        ans = 0
        num1 = 1
        while ans < K:
            if num1 % 5 != 0:
                ans += 1
            else:
                temp = num1
                while temp:
                    ans += 1
                    temp //= 5
            num1 += 1
        print(ans,end=" ")
        return 5 if ans == K else 0

a = Solution()
for i in range(100):
    q = a.preimageSizeFZF(i)
    # print(q,end=" ")
    if i % 10 == 9:
        print()