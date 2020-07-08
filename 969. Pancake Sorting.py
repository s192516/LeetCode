#-*- coding:utf-8 -*-
#@Date   : 2019/1/6
#@Author : suyifan
#@File   : 969. Pancake Sorting.py

A = [3,2,4,1]
class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        min1 = min(A)
        final = sorted(A)
        temp = final[:]
        # list1 = [1,2,3,4]
        # print(final == list1)
        ans = []
        while final != A:
            n = len(temp) - 1
            max1 = max(temp)
            temp.remove(max1)
            idx1 = A.index(max1)
            # print(idx1)
            ans.append(idx1+1)
            ans.append(n+1)
            self.slove(A,idx1)
            self.s1(A,n)


        return ans

    def s1(self,A,n):
        left = 0
        while left < n:
            A[left],A[n] = A[n],A[left]
            left += 1
            n -= 1

    def slove(self,A,idx1):
        left = 0
        while left < idx1:
            A[left],A[idx1] = A[idx1],A[left]
            left += 1
            idx1 -= 1



a = Solution()
q = a.pancakeSort(A)
print("q =",q)