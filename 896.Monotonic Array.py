#-*- coding:utf-8 -*-
#@Date   : 2018/9/5
#@Author : huali
#@File   : 896.Monotonic Array.py

A = [1,1,2,2,2,3]
A = [1,2,2,3]
A = [1,1,1]
A = [1,3,2]
A = [1,2,4,5]
A = [6,5,4,4]
A = [3,4,2,3]

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        rtype = True
        length = len(A)

        if length == 1:
            return rtype
        elif A[0] == A[-1]:
            for i in range(length-1):
                if A[i] != A[i+1]:
                    return False



        if A[0] < A[-1]:
            for i in range(length-1):
                if A[i] <= A[i+1]:
                    continue
                else:
                    return False

        if A[0] > A[-1]:
            for i in range(length-1):
                if A[i] >= A[i+1]:
                    continue
                else:
                    return False

        return rtype
a = Solution()
q = a.isMonotonic(A)
print("q= ",q)