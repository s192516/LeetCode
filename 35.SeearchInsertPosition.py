#-*- coding:utf-8 -*-
#@Date   : 2018/9/2
#@Author : huali
#@File   : 35.SeearchInsertPosition.py

# nums =[1,2,3]
#
# target =2
#
# class Solution:
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         left = 0
#         right = len(nums)
#         rtype =self.searchInsertHelper(left,right-1,nums, target)
#
#         return rtype
#
#     def searchInsertHelper(self,left,right,nums,target):
#
#         middle = (left+right)//2
#         if left < right:
#             self.searchInsertHelper(left,middle,nums,target)
#             self.searchInsertHelper(middle+1,right,nums,target)
#             rtype = self.merge(left,middle,right,nums,target)
#             return rtype
#         else:
#             if nums[left]>=target:
#                 return left
#             else :
#                 return left+1
#     def merge(self,left,middle,right,nums,target):
#         for i in range(left,right+1):
#             # print(left,right,i)
#
#             if nums[i] >=  target:
#             #     if i ==0:
#                 return i
#             #     # else:
#             #     #     return i
#             if i ==len(nums)-1:
#                 return len(nums)


nums =[1,3,5,6]
target =0

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left =0
        right = len(nums)-1

        for i in range(len(nums)):
            if nums[i]>= target:
                return i
            # if nums[right] >=target and nums[right-1] < target:
            if nums[right] < target:
                return right+1



a = Solution()
q =a.searchInsert(nums,target)

print(q)
