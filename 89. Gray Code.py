#-*- coding:utf-8 -*-
#@Date   : 2018/10/12
#@Author : suyifan
#@File   : 89. Gray Code.py

n = 3

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        rtype = []
        i = 1
        return self.solve(rtype, n, i)

    def solve(self, rtype, n, i):
        if i > n:
            return rtype
        if i == 1:
            rtype.append(0)
            rtype.append(1)

        else:
            # length = len(rtype)
            count = 2 ** (i - 1)
            for j in range(count -1 , -1, -1):
                rtype.append(count + rtype[j])
        rtype = self.solve(rtype, n, i + 1)
        return rtype

a = Solution()
q = a.grayCode(n)
print("q =",q)