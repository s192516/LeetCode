#-*- coding:utf-8 -*-
#@Date   : 2018/12/26
#@Author : suyifan
#@File   : 649. Dota2 Senate.py

# senate = "RD"
# senate = "RDD"
# senate = "R"
# senate = "RRRDDDDD"


# -------------------------暴力解法结果正确但是时间超了,而且还可以在优化
# class Solution:
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
#
#         r = d = 0
#         for i in senate:
#             if i == "R":
#                 r += 1
#             else:
#                 d += 1
#
#         n = len(senate)
#         have_right = [True for _ in range(n)]
#
#
#         if r == 0:
#             return "Dire"
#         if d == 0:
#             return "Radiant"
#         while True:
#             # if idx == n:
#             # idx = 0
#             for i in range(n):
#                 if have_right[i]:
#                     b = False
#                     for j in range(i+1, n):
#                         if senate[i] != senate[j] and have_right[j]:
#                             have_right[j] = False
#                             if senate[j] == "R":
#                                 if r == 1:
#
#                                     return "Dire"
#                                 else:
#                                     r -= 1
#                             else:
#                                 if d == 1:
#                                     return "Radiant"
#                                 else:
#                                     d -= 1
#                             b = True
#                             break
#                     if not b:
#                         for j in range(i):
#                             if senate[i] != senate[j] and have_right[j]:
#                                 have_right[j] = False
#                                 if senate[j] == "R":
#                                     if r == 1:
#                                         print(have_right)
#
#                                         return "Dire"
#                                     else:
#                                         r -= 1
#                                 else:
#                                     if d == 1:
#
#                                         return "Radiant"
#                                     else:
#                                         d -= 1
#                                 break
















        # while r and d :
    #     while True:
    #         # if idx == n:
    #         # idx = 0
    #         for i in range(n):
    #             if have_right[i]:
    #                 a = self.close(senate,i+1,n,have_right,r,d)
    #                 if a and a != "already":
    #                     return a
    #                 elif not a:
    #                     b = self.close(senate,0,i,have_right,r,d)
    #                     if b and b != "already":
    #                         return b
    #
    # def close(self,senate,begin, end,have_right,r,d):
    #     for j in range(begin,end):
    #         if senate[begin] != senate[j] and have_right[j]:
    #             have_right[j] = False
    #             if senate[j] == "R":
    #                 if r == 1:
    #                     return "Dire"
    #                 else:
    #                     r -= 1
    #             else:
    #                 if d == 1:
    #                     return "Raniant"
    #                 else:
    #                     d -= 1
    #             return "already"
    #     return False

#
# a = Solution()
# q = a.predictPartyVictory(senate)
# print("q =",q)



senate = "RD"
senate = "RDD"
senate = "R"
senate = "RRRDDDDD"


class Solution:
    def predictPartyVictory(self, senate):

        stack_r = []
        stack_d = []
        for i ,c in enumerate(senate):
            if c == "R":
                stack_r.append(i)
            else:
                stack_d.append(i)

        n = len(senate)
        while stack_d and stack_r:
            a = stack_d.pop(0)
            b = stack_r.pop(0)
            if a < b:
                stack_d.append(a+n)
            else:
                stack_r.append(b+n)

        if stack_d:
            return "Dire"
        else:
            return "Radiant"

a = Solution()
q = a.predictPartyVictory(senate)
print("q =", q)