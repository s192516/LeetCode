#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 477. Total Hamming Distance.py



nums = [4,14,2]

class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        rtype = 0
        while max1 != 0:
            count_0 = count_1 = 0
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    count_0 += 1
                else:
                    count_1 += 1
                nums[i] //= 2
            max1 //= 2
            rtype += count_0 * count_1
        return rtype

a = Solution()
q = a.totalHammingDistance(nums)
print("q = ",q)