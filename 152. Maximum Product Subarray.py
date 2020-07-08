#-*- coding:utf-8 -*-
#@Date   : 2018/10/26
#@Author : suyifan
#@File   : 152. Maximum Product Subarray.py

nums = [3,-1,4]
nums = [-4,-3,-2]
# ---------------------------------------------什么呀这都是???!!!----------
# class Solution:
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         rtype = [0 for _ in range(n)]
#         max1 = 0
#         min1 = 0
#         min2 = 1
#
#         for i in range(n):
#             if i == 0:
#                 num = nums[0]
#                 rtype[0] = num
#             elif rtype[i - 1] == 0:
#                 num = nums[i]
#                 rtype[i] = num
#                 min1 = min1 / min2
#                 min2 = 1
#             else:
#                 num = nums[i] * rtype[i - 1]
#                 rtype[i] = num
#             if num > 0 and num > max1:
#                 max1 = num
#             if num < 0:
#                 if (num / min2) < min1:
#                     min1 = num / min2
#                 elif num > min2:
#                     min2 = num
#         # print(max1,min1,min2)
#         return max(max1, min1)
#
# a = Solution()
# q = a.maxProduct(nums)
# print("q =",q)


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n == 1:
            return nums[0]

        max1, min1, ans = 0, 0, 0
        for num in nums:
            if num > 0:
                max1 = max(max1 * num, num)
                min1 = min(min1 * num, num)
            elif num <= 0:
                temp = max1
                max1 = max(min1 * num, num)
                min1 = min(temp * num, num)
            ans = max(ans, max1)
        return ans

#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         # rtype = [0 for _ in range(n)]
#         max1 = 0
#         min1 = 0
#         rtype = 0

#         for num in nums:
#             if num >= 0:
#                 max1 = max(num,max1 * num)
#                 min1 = min(num,min1 * num)
#             else:
#                 temp = max1
#                 max1 = max(num,min1 * num)
#                 min1 = min(num,temp * num)
#             rtype = max(rtype,max1)
#         return rtype

a = Solution()
q = a.maxProduct(nums)
print("q =",q)