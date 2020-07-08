#-*- coding:utf-8 -*-
#@Date   : 2018/12/2
#@Author : suyifan
#@File   : 949. Largest Time for Given Digits.py

A = [1,2,3,4]
A = [5,5,5,5]
A = [0,0,0,0]
A = [0,0,4,0]
A = [2,0,6,6]
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        # if 2 in A:
        #     ans = "2"
        # elif 1 in A:
        #     ans = "1"
        # elif 0 in A:
        #     ans = "0"
        # q = A.index(int(ans))
        # A.pop(q)

        # ans = ""
        # have = False
        # for i in range(2, -1,-1):
        #     if i in A:
        #         ans += str(i)
        #         q = A.index(i)
        #         A.pop(q)
        #         have = True
        #         break
        # if not have:
        #     return ""
        #
        # have = False
        # if ans == "2":
        #     k = 3
        # else:
        #     k = 9
        # for i in range(k, -1,-1):
        #     if i in A:
        #         ans += str(i)
        #         q = A.index(i)
        #         A.pop(q)
        #         have = True
        #         break
        # if not have:
        #     return ""
        #
        # ans += ":"
        #
        # have = False
        # for i in range(5, -1,-1):
        #     if i in A:
        #         ans += str(i)
        #         q = A.index(i)
        #         A.pop(q)
        #         have = True
        #         break
        # if not have:
        #     return ""
        #
        #
        # ans += str(A[0])
        # return ans
        dictA = {}
        for i in A:
            dictA[str(i)] = dictA.get(str(i),0) + 1
        for i in range(23,-1,-1):
            for j in range(59,-1,-1):
                dict1 = {}
                if i < 10:
                    i1 = "0"+str(i)
                else:
                    i1 = str(i)
                if j < 10:
                    j1 = "0"+str(j)
                else:
                    j1 = str(j)
                str1 = str(i1) + str(j1)

                for q in str1:
                    dict1[q] = dict1.get(q,0) + 1
                count = 0

                for k,v in dictA.items():

                    if dict1.get(k,0) != v:
                        break
                    count += v

                # print(i,j)
                if count == 4:
                    return str(i1)+ ":"+str(j1)
        return ""

a = Solution()
q = a.largestTimeFromDigits(A)
print("q =",q)