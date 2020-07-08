#-*- coding:utf-8 -*-
#@Date   : 2018/11/18
#@Author : suyifan
#@File   : 474. Ones and Zeroes.py



strs = ["10", "0001", "111001", "1", "0"]
# strs = ["10", "0001", "1", "0", "111001"]
# strs = ["1","0"]
strs = ["10", "0001", "111001", "1", "0","0101101","10101","101"] # 10,1,0,101,10101

#m 代表0 ,n代表1
m = 6 # 答案5
n = 9
m = 4 # 答案3
n = 4

strs = ["10","0001","111001","1","0"] #答案3
m = 4
n = 3
# strs = ["10","0001","111001","1","0"] #答案4
# m = 5
# n = 3

strs = ["011","1","11","0","010","1","10","1","1","0","0","0","01111","011","11","00","11","10","1","0","0","0","0","101","001110","1","0","1","0","0","10","00100","0","10","1","1","1","011","11","11","10","10","0000","01","1","10","0"] # ans = 45
m = 44
n = 39

# class Solution:
#     def __init__(self):
#         self.have = False
#
#     def findMaxForm(self, strs, m, n):
#         """
#         :type strs: List[str]
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         length = len(strs)
#         dp = [0 for _ in range(length)]# * n
#
#         def solve(m,n,left):
#             if m < 0 or n < 0 :#or left == length :
#                 return 0
#             if m >=0 and n>=0 and left == length :
#                 self.have = True
#                 print("yes")
#                 return 0
#             # elif left == length:
#             #     return 0
#
#             m0,n1 = self.count(strs[left])
#             if dp[left] != 0:
#                 return dp[left]
#
#             # if m-m0 >=0 and n-n1>=0 :#and left+1<length:
#             dp[left] = max(1+solve(m-m0,n-n1,left+1),solve(m,n,left+1))
#             # else:
#             #     dp[left] = solve(m,n,left+1)
#             print(dp)
#             return dp[left]
#         # print(dp)
#         return solve(m,n,0)
#
#
#
#
#     def count(self, num):
#         m0 = n1 = 0
#         for i in num:
#             if i == "0":
#                 m0 += 1
#             else:
#                 n1 += 1
#         return m0, n1
#
# print("strs =", strs)
# a = Solution()
# q = a.findMaxForm(strs,m,n)
# print("q =",q)

# class Solution:
#     def __init__(self):
#         self.have = False
#
#     def findMaxForm(self, strs, m, n):
#         """
#         :type strs: List[str]
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         length = len(strs)
#         dp = [0 for _ in range(length)]# * n
#         dp = self.solve(strs,dp,length,0,m,n)
#         return dp
#
#     def solve(self,strs,dp,length,left,m,n):
#         # print(dp)
#
#         if m < 0 or n < 0 or left <0:
#             return 0
#         if dp[left]:
#             return dp[left]
#
#         for i in range(left,length):
#             m0, n1 = self.count(strs[i])
#             # print(m0,n1)
#             # if m-m0>=0 and n-n1>=0:
#             # m -= m0
#             # n -= n1
#             dp[i] = max(1+self.solve(strs,dp,length,i-1,m-m0,n-n1),self.solve(strs,dp,length,i-1,m,n))
#             # else:
#             #     dp[i] =  self.solve(strs,dp,length,left-1,m,n)
#             print(dp)
#         return dp[-1]
#
#
#     def count(self, num):
#         m0 = n1 = 0
#         for i in num:
#             if i == "0":
#                 m0 += 1
#             else:
#                 n1 += 1
#         return m0, n1
#
# print("strs =", strs,m,n)
# a = Solution()
# q = a.findMaxForm(strs,m,n)
# print("q =",q)

# class Solution:
# #     # def __init__(self):
# #     #     self.ans = 0
# #
# #     def findMaxForm(self, strs, m, n):
# #         length = len(strs)
# #         dp = [-1 for _ in range(length)]# * n
# #
# #         def solve(m,n,left):
# #             if m < 0 or n < 0 :#or left == length :
# #                 # print(left,"return")
# #                 return -1
# #             if m >= 0 and n >= 0 and left == length:
# #                 print("yes")
# #                 return 1
# #             elif left == length:
# #                 print("return")
# #                 return 0
# #
# #             m0,n1 = self.count(strs[left])
# #             if dp[left] != -1:
# #                 return dp[left]
# #
# #             # if m-m0>=0 and n-n1 >=0:
# #             dp[left] = max(1+solve(m-m0,n-n1,left+1),solve(m,n,left+1))
# #             # else:
# #             #     dp[left] = solve(m,n,left+1)
# #             print(dp)
# #             return dp[left]
# #
# #         print(dp)
# #         return solve(m,n,0)
# #
# #
# #     def count(self, num):
# #         m0 = n1 = 0
# #         for i in num:
# #             if i == "0":
# #                 m0 += 1
# #             else:
# #                 n1 += 1
# #         return m0, n1
# #
# # print("strs =", strs,m,n)
# # a = Solution()
# # q = a.findMaxForm(strs,m,n)
# # print("q =",q)

#-------------------------------------------二维矩阵------------------
class Solution:
    # def __init__(self):
    #     self.ans = 0

    def findMaxForm(self, strs, m, n):
       # dp = [ [-1 for i in range(m)] for j in range(n)]
        dict1 = {}
        for s in strs:
            m0,n1 = self.count(s)
            if m0<=m and n1<=n:
                dict2 = {}
                for k,v in dict1.items():
                    x,y = k[0],k[1]
                    a,b = m0+x,n1+y
                    if a <= m and b<=n:
                        dict2[(a,b)] = max(dict1.get((a,b),0),dict1.get((x,y),0)+1) #+dict1.get((m0,n1),1)
                dict1[(m0,n1)] = dict1.get((m0,n1),1)
                dict1.update(dict2)
        ans = 0
        list1 = []
        for v in dict1.values():
            list1.append(v)
            ans = max(v,ans)
        print(sorted(list1,reverse=True))
        # count = 0
        # dict1 = sorted(dict1.items(),key=lambda item:item,reverse=True)
        # print(dict1)
        # for i in dict1:
        #     count += 1
        #     if count % 5 == 0:
        #         print()
        #     print(i,end="--")
        # for k,v in dict1.items():
        #     count += 1
        #     if count % 5 == 0:
        #         print()
        #     print((k,v),end="  ")
        # list_dp = []
        # for s in strs:
        #     m0,n1 = self.count(s)
        #     if m0<=m and n1<= n:
        #         temp = []
        #         for arr in list_dp:
        #             x,y,z = arr[0],arr[1],arr[2]
        #             a,b = m0+x,n1+y
        #             if a <= m and b<= n:
        #                 arr[]

        return ans


    def count(self, num):
        m0 = n1 = 0
        for i in num:
            if i == "0":
                m0 += 1
            else:
                n1 += 1
        return m0, n1


print("strs =", strs,m,n)
a = Solution()
q = a.findMaxForm(strs,m,n)
print("q =",q)