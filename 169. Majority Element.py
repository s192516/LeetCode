#-*- coding:utf-8 -*-
#@Date   : 2018/9/14
#@Author : suyifan
#@File   : 169. Majority Element.py

nums = [1,1,1,1,2,2,2,2,2]
nums = [1,2,3,3]
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for i in nums:
            # print(dict1)
            if i in dict1:
               if dict1[i] + 1 > len(nums) / 2:
                   return i
               else:
                   dict1[i] += 1
            else:
                dict1[i] = 1
        if dict1[i] + 1 >= len(nums) / 2:
            return i

a =Solution()
q = a.majorityElement(nums)
print("q=",q)