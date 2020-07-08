#-*- coding:utf-8 -*-
#@Date   : 2018/11/18
#@Author : suyifan
#@File   : 941. Valid Mountain Array.py

A = [2,1]
# A = [0,3,2,1]
A = [3,5,5]
A = [0,1,2,3,4,5,6,7,8,9]
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        change = False
        have = False
        n = len(A)
        if n < 3:
            return False

        for i in range(n - 1):
            if not change:
                if A[i] < A[i + 1]:
                    have = True
                    continue
                elif A[i] > A[i + 1]:
                    change = True
                else:
                    return False
            else:
                if A[i] <= A[i + 1]:
                    return False
        if have and change:
            return True
        else:
            return False



a = Solution()
q = a.validMountainArray(A)
print("q =",q)