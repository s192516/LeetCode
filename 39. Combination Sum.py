#-*- coding:utf-8 -*-
#@Date   : 2018/10/10
#@Author : suyifan
#@File   : 39. Combination Sum.py

# candidates = [3,2,1]
# target = 5
#
#
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
#                 temp.append(candidates[i])
#                 self.solve(candidates,target,length,i,sum + candidates[i],temp,rtype)
#                 temp.pop()
#                 i += 1
#         return rtype
#         # import copy
#         #
#         # while i < length:
#         #     sum += candidates[i]
#         #     temp.append(candidates[i])
#         #     if sum < target:
#         #         # temp.append(candidates[i])
#         #         self.solve(candidates,target,length,i,sum,temp)
#         #     elif sum == target:
#         #         # temp.append(candidates[i])
#         #         self.rtype.append(copy.deepcopy(temp))
#         #         temp.pop()
#         #
#         #     else:
#         #         sum -= candidates[i]
#         #         temp.pop()
#         #
#         #         self.solve(candidates,target,length,i+1,sum,temp)
#         #
#         #     i += 1
#
#
#
#
#
# a = Solution()
# q = a.combinationSum(candidates,target)
# print("q =",q)




candidates = [3,2,1,4,5,9,7]
target = 10



class Solution:

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        left = 0
        right = candidates.__len__()
        rtype = []
        temp = []
        candidates.sort()
        return self.solve(candidates, left, right, target, rtype, temp)

    def solve(self, candidates, left, right, target, rtype, temp):
        if target == 0:
            rtype.append(temp[:])
            return rtype

        elif target > 0:
            for i in range(left,right):
                temp.append(candidates[i])
                target -= candidates[i]
                rtype[:] = self.solve(candidates, i+ 1, right, target, rtype, temp)
                temp.pop()
                target += candidates[i]
        return rtype

a = Solution()
q = a.combinationSum(candidates,target)
print("q =",q)
