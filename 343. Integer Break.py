#-*- coding:utf-8 -*-
#@Date   : 2018/12/31
#@Author : suyifan
#@File   : 343. Integer Break.py

n = 5
n = 56

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(2,n+1):
            left = 1
            right = i - left
            max1 = 0
            while left <= right:
                max1 = max(max(dp[left],left)*max(dp[right],right),max1)
                left += 1
                right -= 1
            dp[i] = max1
        # print(dp)
        return dp[-1]
a = Solution()
q = a.integerBreak(n)
print("q =",q)