#-*- coding:utf-8 -*-
#@Date   : 2018/12/19
#@Author : suyifan
#@File   : 775. Global and Local Inversions.py


A = [1,3,2,4,5,0]
# A = [0,1,3,2,4,5]
# A = [1,0,2]
# A = [1,2,0]
# A = [1,2,0,3]
class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # part = 0
        n = len(A)
        # for i in range(len(A) - 1):
        #     if A[i] > A[i + 1]:
        #         part += 1
        # all_num = 0

        count = A[-1]
        list1 = [None] * n
        for i, num in enumerate(reversed(A)):
            if count > num:
                count = num
            list1[n - i - 1] = count


        print(list1)
        for i in range(len(A) - 2):
            if A[i] > list1[i+2]:
                return False
            if A[i] > A[i + 1] :
                if not A[i] < list1[i+2]:
                    return False
        return True
        # for i in range(len(A) - 1):
        #     for j in range(i + 1, n):
        #         if A[i] > A[j]:
        #             all_num += 1
        #         if all_num > part:
        #             return False
        # print(part,all_num,len(A))
        # return part == all_num

a = Solution()
q = a.isIdealPermutation(A)
print("q =",q)