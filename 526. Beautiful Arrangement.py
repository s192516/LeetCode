#-*- coding:utf-8 -*-
#@Date   : 2018/12/28
#@Author : suyifan
#@File   : 526. Beautiful Arrangement.py



N = 5
N = 15

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [None] * N
        set1 = set()
        self.ans = 0
        self.solve(dp,N,N,set1)
        return self.ans

    def solve(self,dp,N,n,set1):
        if n == 1 :
            self.ans += 1
            return
        for i in range(N,0,-1):
            if (i not in set1 )and ((i % n == 0) or (n % i == 0) ):
                # dp[i] = i
                set1.add(i)
                self.solve(dp,N,n-1,set1)
                set1.remove(i)

a = Solution()
q = a.countArrangement(N)
print("q =",q)

