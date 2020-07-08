#-*- coding:utf-8 -*-
#@Date   : 2018/10/14
#@Author : suyifan
#@File   : 665. Non-decreasing Array.py

nums = [2,3,3,2,4]
nums = [2,3,3,2,4,1]
nums = [-1,4,2,3]
nums = [1,4,2,3]
nums = [4,2,3]
nums = [1,2,3,4,2]
nums = [3,4,2,3]

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # change = False
        # rtype = True
        length = len(nums)
        # change = False
        num = nums[1]
        if nums[0] <= nums[1]:
            change = False
        else:
            change = True

        for i in range(2,length):
            if nums[i] >= num:
                num = nums[i]
            else:
                if not change:
                    change = True
                else:
                    return False
                if nums[i] < nums[i-2]:
                    # if i != length -1:
                    num = nums[i -1]
                    # else:
                    #     return  True
                else:
                    num = nums[i]
        return True



print(nums)
a = Solution()
q = a.checkPossibility(nums)
print("q =",q)