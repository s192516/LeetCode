#-*- coding:utf-8 -*-
#@Date   : 2018/9/9
#@Author : suyifan
#@File   : 217. Contains Duplicate.py


# nums = [1,2,3,1]
#
# class Solution:
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         set1 = set(nums)
#         print("set1= ",set1)
#         print("nums=",nums)
#
#         if len(set1) == len(nums):
#             return False
#         else :
#             return True
#
# a = Solution()
# q = a.containsDuplicate(nums)
# print("q= ",q)



nums = [1,2,3,4]

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = []
        for i in nums:
            if i in set1 :
                return True
            else:
                set1.append(i)
        return False


a = Solution()
q = a.containsDuplicate(nums)
print("q= ",q)