#-*- coding:utf-8 -*-
#@Date   : 2018/10/10
#@Author : suyifan
#@File   : 40. Combination Sum II.py




candidates = [3,2,1]
target = 5

candidates = [2,5,2,1,2]
target = 5
class Solution:

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list1 = [[]]
        rtype = []
        candidates.sort()
        for num in candidates:
            temp_list = list1[:]
            # sum1 = 0
            for temp in temp_list:
                q = temp[:]
                q.append(num)
                sum1 = sum(q)
                if q not in list1:
                    list1.append(q)
                if sum1 == target:
                    if q not in rtype:
                        rtype.append(list1[-1])
                    else:
                        list1 = list1[:-1]
                elif sum1 > target:
                    list1 = list1[:-1]
        return rtype


    # def solve(self,candidates,target,length,i,sum,temp,rtype):



a = Solution()
q = a.combinationSum(candidates,target)
print("q =",q)




# class Solution:
#     def __init__(self):
#         self.rtype = []
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         sum = 0
#         length = len(candidates)
#         i = 0
#         temp = []
#         rtype = []
#         candidates.sort()
#         print(candidates)
#         return self.solve(candidates,target,length,i,sum,temp,rtype)
#         # return self.rtype
#
#     def solve(self,candidates,target,length,i,sum,temp,rtype):
#         import copy
#
#         if sum == target:
#             rtype.append(copy.deepcopy(temp))
#             # rtype.append(temp)
#
#         else:
#             while i < length and sum + candidates[i]<= target:
#             # while sum + candidates[i] <= target:
#                 temp.append(candidates[i])
#
#                 self.solve(candidates,target,length,i+ 1,sum + candidates[i],temp,rtype)
#                 pop = temp.pop()
#                 print(pop,candidates[i + 1])
#                 while i < length-1 and candidates[i + 1] != pop:
#                     i += 1
#                 i += 1
#
#         return rtype
#
#
# a = Solution()
# q = a.combinationSum(candidates,target)
# print("q =",q)