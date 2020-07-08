#-*- coding:utf-8 -*-
#@Date   : 2019/1/13
#@Author : suyifan
#@File   : 491. Increasing Subsequences.py

nums = [4,6,7,7]
class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        for i1,num1 in enumerate(nums):
            temp = [num1]
            for i2 in range(i1+1,n):
                if nums[i2] >= temp[-1]:
                    temp.append(nums[i2])
                    ans.append(temp[:])
        return ans



a = Solution()
q = a.findSubsequences(nums)
print("q =",q)