#-*- coding:utf-8 -*-
#@Date   : 2018/9/14
#@Author : suyifan
#@File   : 229. Majority Element II.py

nums =[1,1,1,3,3,2,2,2]
# nums = [1,1,1,1,1]
# nums = [1,2]
nums =[1,1,1,3,3,2,2,2,2]
nums = [1,2,1,2,3]

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        lenth=len(nums)
        index=0
        count=1
        for i in range(lenth):
            if nums[index]==nums[i]:
                count+=1
            else:
                count-=1
            if count==0:
                index=i
                count+=1
        return nums[index]


a = Solution()
q = a.majorityElement(nums)
print("q=",q)