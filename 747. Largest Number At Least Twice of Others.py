#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 747. Largest Number At Least Twice of Others.py


nums = [1, 2, 3, 4]
nums = [1]
nums = [1,2]
nums = [3, 6, 1, 0]
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            max1,min1 = nums[0],nums[1]
            i = 0
        else:
            max1,min1 = nums[1],nums[0]
            i = 1
        j = 2
        while j < len(nums):
            if nums[j] > max1:
                max1,min1 = nums[j],max1
                i = j
                j += 1
                continue
            if nums[j] > min1 :
                min1 = nums[j]
                j += 1
                continue
            j += 1
        # print(max1,min1)
        if max1 >= 2 * min1:
            return i
        else :
            return  -1



a = Solution()
q = a.dominantIndex(nums)
print("q=",q)