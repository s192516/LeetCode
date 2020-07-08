#-*- coding:utf-8 -*-
#@Date   : 2018/11/30
#@Author : suyifan
#@File   : 41. First Missing Positive.py



nums = [-1,4,3,1]

nums = [3,4,-1,1]
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] < (n + 1) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        # print(nums)
        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1
        return n + 1

a = Solution()
q = a.firstMissingPositive(nums)
print("q =",q)