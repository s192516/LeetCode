#-*- coding:utf-8 -*-
#@Date   : 2019/1/13
#@Author : suyifan
#@File   : 976. Largest Perimeter Triangle.py

A = [2,3,3,4]
A = [3,6,2,3]
# A = [1,2,1]
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)< 3:
            return 0
        a = max(A)
        A.remove(a)
        # print(A)
        b = max(A)
        A.remove(b)

        while A:
            c = max(A)

            if a - b < c:
                return a+b+c
            else:
                A.remove(c)
                a,b = b,c
        return 0



a = Solution()
q = a.largestPerimeter(A)
print("q=",q)