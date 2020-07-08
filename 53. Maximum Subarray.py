#-*- coding:utf-8 -*-
#@Date   : 2018/9/14
#@Author : suyifan
#@File   : 53. Maximum Subarray.py

nums = [1,2,3,-4,5,-6,7,-8]
nums = [-1]
nums = [2]
nums = [-2,-100,-1]
nums = [-1,1,2,1]
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2,3,1,3]
nums = [2,2]
nums = [-2,1,-3,4,-1,2,1,-5,4]



##### 需要注意的点好多啊,首先在线处理是一个比分而治之还要快的算法
##### 其次,在处理时候需要注意数组为1的情况,但不需要考虑数组为0的情况
##### 当输出最小值小于0的时候输出最小值而不是0
##### 不需要考虑数组为空的情况

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sum = nums[0]
        for i in nums:

            if sum < 0:
                if max_sum <= 0:
                    # sum = max(i,sum + i)
                    sum = i
                else:
                    sum = max(0,i)
            else:
                sum += i

            if sum > max_sum:
                max_sum = sum

        return max_sum



a = Solution()
q = a.maxSubArray(nums)
print("q=",q)


# nums = [1,2,3,-4,5,-6,7,-8]
# nums = [-1]
# nums = [2]
# nums = [-2,-100,-1]
# nums = [-1,1,2,1]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2,3,1,3]
# nums = [2,2]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
#
# class Solution:
#     def maxSubArray(self, nums):
#
#         right = len(nums) - 1
#         return self.maxSubArray_Helper(nums,0,right)
#
#     def maxSubArray_Helper(self,nums,left,right):
#
#
#         if (left == right):
#             return nums[left]
#
#         if left < right:
#            middle = (left + right) //2
#            max_left = self.maxSubArray_Helper(nums,left,middle)
#            max_right = self.maxSubArray_Helper(nums,middle+1,right)
#
#         temp_max_left = 0
#         temp_sub_left = nums[middle]
#         for  i in range(middle,left-1,-1):
#            temp_max_left += nums[i]
#            if temp_max_left > temp_sub_left:
#                 temp_sub_left = temp_max_left
#
#         temp_max_right = 0
#         temp_sub_right = nums[middle + 1]
#         for i in range( middle+1,right+1):
#             temp_max_right += nums[i]
#             if temp_max_right > temp_sub_right:
#                 temp_sub_right = temp_max_right
#
#         return max(max_right,max_left,temp_sub_left+temp_sub_right)
#
#
#
#
#
# a = Solution()
# q = a.maxSubArray(nums)
# print("q=",q)

