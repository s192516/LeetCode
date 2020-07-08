#-*- coding:utf-8 -*-
#@Date   : 2018/12/9
#@Author : suyifan
#@File   : 955. Delete Columns to Make Sorted II.py


A = ["doeeqiy","yabhbqe","twckqte"]


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        length = len(A)
        width = len(A[0])
        ans = 0
        list1 = [None] * length
        for j in range(width ):
            temp = []
            for i in range(length-1):
                if not list1[i] :
                    if ord(A[i][j]) < ord(A[i+1][j]):
                        # list1[i] = True
                        temp.append(i)
                    if ord(A[i][j]) > ord(A[i+1][j]):
                        ans += 1
                        # list1[i] = False
                        temp = []
                        break
            while temp:
                list1[temp.pop()] = True
        return ans


a = Solution()
q = a.minDeletionSize(A)
print("q =",q)