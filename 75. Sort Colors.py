#-*- coding:utf-8 -*-
#@Date   : 2018/10/20
#@Author : suyifan
#@File   : 75. Sort Colors.py


nums = [2,0,2,1,1,0]
nums = [0,0]
nums = [2,0,1]
nums = [1,2,0]

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        right = len(nums) - 1

        idx = 0
        left = 0
        # if right == 2:

        while idx <= right:
            while left < right and nums[left] == 0:
                left += 1
            if idx < left:
                idx = left
            while idx <= right and nums[idx] == 1:
                idx += 1
            while idx <= right and nums[right] == 2:
                right -= 1
            if idx <= right and nums[idx] == 0:
                nums[left], nums[idx] = nums[idx], nums[left]
                left += 1
                idx += 1
            elif idx <= right:
                nums[right], nums[idx] = nums[idx], nums[right]
                right -= 1
                # idx += 1

            # while idx <= right and nums[left] == 0:
            #     left += 1
            #     idx += 1
            # while idx <= right and nums[right] == 2:
            #     right -= 1
            # while idx <= right and  nums[idx] == 1:
            #     idx += 1
            # if nums[idx] == 0:
            #     nums[left],nums[idx] = nums[idx],nums[left]
            #     left += 1
            #     idx += 1
            # elif nums[idx] == 2:
            #     nums[right],nums[idx] = nums[right],nums[idx]
            #     right -= 1
            #     idx += 1

a = Solution()
q = a.sortColors(nums)
print(nums)
