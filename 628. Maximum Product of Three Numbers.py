#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 628. Maximum Product of Three Numbers.py

nums = [1,2,3,4]
# nums = [1,2,3]
##### 注意负号!!!!!
##### 注意0!!!!
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx_max2 = max(nums[0],nums[1],nums[2])
        idx_max0 = min(nums[0],nums[1],nums[2])
        idx_max1 = nums[0] + nums[1] + nums[2] - idx_max0 - idx_max2

        idx_min2 = min(nums[0], nums[1], nums[2])
        idx_min0 = max(nums[0], nums[1], nums[2])
        idx_min1 = nums[0] + nums[1] + nums[2] - idx_max0 - idx_max2

        # print(idx_max0,idx_max1,idx_max2,idx_min0,idx_min1,idx_min2)

        for i in nums[3:]:
            if i > idx_max2:
                idx_max2,idx_max1,idx_max0 = i,idx_max2,idx_max1
            elif i > idx_max1:
                idx_max1,idx_max0 = i,idx_max1
            elif i > idx_max0:
                idx_max0 = i


            if i < idx_min2:
                idx_min2, idx_min1, idx_min0 = i, idx_min2, idx_min1
            elif i < idx_min1:
                idx_min1, idx_min0 = i, idx_min1
            elif i < idx_min0:
                idx_min0 = i


        max1 = idx_max0 * idx_max1 * idx_max2
        min1 = idx_min0 * idx_min1 * idx_min2
        mix1 = idx_max2 * idx_min2 * idx_min1
        # print(max1,min1,mix1)
        return max(max1,min1,mix1)



        # return [idx_max0,idx_max1,idx_max2,idx_min0,idx_min1,idx_min2]

a = Solution()
q = a.maximumProduct(nums)
print("q=",q)
