#-*- coding:utf-8 -*-
#@Date   : 2018/10/25
#@Author : suyifan
#@File   : 137. Single Number II.py


nums = [2,2,2,3]
# nums = [7,7,7,5]
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
nums = [-19,-46,-19,-46,-9,-9,-19,17,17,17,-13,-13,-9,-13,-46,-28]
nums = [-28]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            temp = 0
            for num in nums:
                q = num >> i
                temp += (num >> i) & 1
            res = res + (temp % 3) * (2 ** i)
        return self.convert(res)

    def convert(self, x):
        if x >= 2 ** 31:
            x -= 2 ** 32
        return x





a = Solution()
q = a.singleNumber(nums)
print("q =",q)