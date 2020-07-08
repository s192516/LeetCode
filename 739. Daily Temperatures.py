#-*- coding:utf-8 -*-
#@Date   : 2019/1/10
#@Author : suyifan
#@File   : 739. Daily Temperatures.py

T = [73,74,75,71,69,72,76,73]

class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        decline = []
        arise = []

        min1 = max1 = T[0]
        stack = []
        ans = [0] * len(T)
        for i,num in enumerate(T):
            if (not stack) or num <= stack[-1][1]:
                stack.append([i,num])
            else:
                while stack:
                    idx,num1 = stack.pop()
                    if num > num1:
                        ans[idx] = i - idx
                    else:
                        stack.append([idx,num1])
                        break
                stack.append([i,num])
        return ans


a = Solution()
q = a.dailyTemperatures(T)
print("q =",q)