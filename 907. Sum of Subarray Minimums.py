#-*- coding:utf-8 -*-
#@Date   : 2018/12/5
#@Author : suyifan
#@File   : 907. Sum of Subarray Minimums.py


A = [1,7,5,2,4,3,9]
A = [3,1,2,4]

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD

a = Solution()
q = a.sumSubarrayMins(A)
print("q =",q)