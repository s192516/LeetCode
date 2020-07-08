#-*- coding:utf-8 -*-
#@Date   : 2018/11/18
#@Author : suyifan
#@File   : 942. DI String Match.py


A = ["cba","daf","ghi"]
A = ["zyx","wvu","tsr"]
# A= ["a","b"]
# A = ["rrjk","furt","guzm"]
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        length = len(A)
        width = len(A[0])
        ans = 0

        for j in range(width ):
            for i in range(length-1):

                if ord(A[i][j]) > ord(A[i+1][j]):
                    ans += 1
                    break
        return ans




a = Solution()
q = a.minDeletionSize(A)
print("q =",q)