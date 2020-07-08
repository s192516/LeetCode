#-*- coding:utf-8 -*-
#@Date   : 2018/9/16
#@Author : suyifan
#@File   : 33. Search in Rotated Sorted Array.py

# import random
# a = random.randint(1,200)
# b = random.randint(0,a)
#
# a = 165
# b = 68
# a = 165
# b = 57
# a = 153
# b = 9
# nums = [i for i in range(1,a+1)]
# nums = nums[b:] +nums[:b]
# target = random.randint(0,a)
# target = 1
# target = 165
# target = 43
# print("a=",a,"b=",b,"target= ",target,"nums=",nums)
# # [1,3]
# # 3
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         if target in nums:
#             left = 0
#             right = len(nums)-1
#             middle = (left + right) // 2
#             while target != nums[middle]:
#                 if nums[right] == target:
#                     return right
#                 if nums[left] < nums[middle]:
#                     if nums[left] < target:
#                         if nums[middle] < target:
#                             left = middle + 1
#                             middle = (left + right) // 2
#                             continue
#                         else:
#                             right = middle - 1
#                             middle = (left + right) // 2
#                             continue
#
#                     elif nums[left] > target:
#                         left = middle + 1
#                         middle = (left + right) // 2
#                         continue
#                     else :
#                         return left
#                 else:
#                     if nums[left] < target:
#                         right = middle - 1
#                         middle = (left + right) // 2
#                         continue
#                     elif nums[left] > target:
#                         if nums[middle] > target:
#                             right = middle - 1
#                             middle = (left + right) // 2
#                             continue
#                         else:
#                             left = middle + 1
#                             middle = (left + right) // 2
#                             continue
#                     else :
#                         return left
#
#
#             return middle
#         else:
#             return -1




# nums = [1,3]
# target = 3



# a = Solution()
# q = a.search(nums,target)
# print("q=",q)



# 正确方法

# nums = [4,5,6,7,1,2,3]
# target = 1
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         # [4,5,6,7,1,2,3]
#         left = 0
#         right = len(nums) - 1
#         while left + 1 < right:
#             mid = (left + right) // 2
#             if nums[mid] == target :
#                 return mid
#             if nums[left] < nums[mid]:
#                 if  nums[left] <= target and nums[mid] >= target:
#                     right = mid
#                 else:
#                     left = mid
#             else:
#                 if nums[right] >= target and nums[mid] <= target:
#                     left = mid
#                 else:
#                     right = mid
#         if nums[left] == target:
#             return left
#         if nums[right] == target:
#             return right
#         return -1
#
# a = Solution()
# q = a.search(nums,target)
# print("q =",q)



### 测试方法
nums = [4,5,6,7,1,2,3]
target = 1
nums = [1]
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # [4,5,6,7,1,2,3]
        left = 0
        right = len(nums) - 1
        while left  < right:
            mid = (left + right) // 2
            if nums[mid] == target :
                return mid
            if nums[left] < nums[mid]:
                if  nums[left] <= target and nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[right] >= target and nums[mid] <= target:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

a = Solution()
q = a.search(nums,target)
print("q =",q)