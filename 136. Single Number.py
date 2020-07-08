#-*- coding:utf-8 -*-
#@Date   : 2018/9/8
#@Author : suyifan
#@File   : 136. Single Number.py

nums = [1,1,2,2,3]
nums = [4,1,2,1,2]

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] +=1
            else :
                dict1[i] = 1

        for key ,value in dict1.items():
            if value == 1:
                return key

        # return dict1



a = Solution()
q = a.singleNumber(nums)
print("q= ",q)