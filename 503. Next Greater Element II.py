#-*- coding:utf-8 -*-
#@Date   : 2018/11/18
#@Author : suyifan
#@File   : 503. Next Greater Element II.py



nums = [2,1,3,5,1]


# class Solution:
#     def nextGreaterElements(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         import collections
#         if not nums:
#             return []
#         n = len(nums)
#         nums = nums * 2
#         dq = collections.deque()  # save index because we need to check if this is in the original nums
#         rst = [-1] * n
#
#         for i, v in enumerate(nums):
#             while dq and nums[dq[-1]] < v:
#                 # if 0 <= dq[-1] < n:
#                 rst[dq[-1]%n] = v
#                 dq.pop()
#             dq.append(i)
#
#         return rst


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        nums = nums * 2
        stack = []
        res = [-1] * n
        for k, v in enumerate(nums):

            while stack and nums[stack[-1]] < v:
                if stack[-1] < n:
                    res[stack[-1] % n] = v
                stack.pop()
            stack.append(k)
        return res


a = Solution()
q = a.nextGreaterElements(nums)
print("q =",q)