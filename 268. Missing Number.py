#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 268. Missing Number.py


nums = [0,1,3]


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        rtype = length * (length + 1) / 2
        for i in range(length):
            rtype -= nums[i]
        return int(rtype)


a = Solution()
q = a.missingNumber(nums)
print("q=",q)