#-*- coding:utf-8 -*-
#@Date   : 2018/9/16
#@Author : suyifan
#@File   : 238. Product of Array Except Self.py



import numpy as np


nums = [1,2,3,4,5]


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        idx_left = 1
        length = len(nums)
        idx_right = length - 1

        list_left = []
        list_right = []

        list_left.append(1)
        list_right.append(1)


        while idx_left < length :

            list_left.append(list_left[idx_left - 1] * nums[idx_left - 1])
            list_right.append(list_right[idx_left - 1] * nums[idx_right - idx_left + 1])
            idx_left += 1

        rtype = []
        for i in range(length):
            rtype.append(list_left[i] * list_right[length - 1 - i])
        return rtype

a = Solution()
q = a.productExceptSelf(nums)
print("q=",q)