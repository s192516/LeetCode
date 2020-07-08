#-*- coding:utf-8 -*-
#@Date   : 2018/9/8
#@Author : suyifan
#@File   : 204. Count Primes.py
#
# n = 4
#
# class Solution:
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         list1 = [2,3]
#         if n <3:
#             return 0
#         elif n <4:
#             return 1
#         elif n <5 :
#             return 2
#         else:
#             for i in range(5,n):
#                 count = 0
#                 for j in list1:
#                     if i % j != 0:
#                         count += 1
#                     else :
#                         break
#                 if count == len(list1):
#                     list1.append(i)
#         return len(list1)


n = 10

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        list1 = []

        # if n < 2:
        #     return 0
        # if n < 3:
        #     return 1

        for i in range(n):
            list1.append(True)
        # list1[0] = False
        # list1[1] = False

        for i in range(2,n):
            if i ** 2 > n :
                break
            if not(list1[i]):
                continue
            for j in range(i ** 2,n,i):
                list1[j] = False

        count = 0
        for i in range(2,n):
            if list1[i] == True:
                count += 1

        return count

        return len(list1)




a = Solution()
q = a.countPrimes(n)
print("q=",q)