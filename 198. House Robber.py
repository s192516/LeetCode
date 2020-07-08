#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 198. House Robber.py

#如果只用递归的话需要运算2的n次方次
#记录下每次运算的结果,免得每次都要重新算
#记录的方法就是新建一个数组...
#此所谓牺牲空间换时间
#最后注意这个数组需要时全局变量
#目前为止还没有完全搞明白变量作用域

# nums1 = [56,95,82,8,45]
# nums1 = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
# nums1 = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
# nums1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# nums1 = []
#
#
# class Solution:
#     # list1 = []
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         global list1
#         list1 = [None for x in range(len(nums))]
#
#         return  self.solve(len(nums) - 1,nums)
#
#
#     def solve(self,idx,nums):
#         if idx < 0:
#             return 0
#
#         if list1[idx] != None :
#             return list1[idx]
#
#         list1[idx] = max(nums[idx] + self.solve(idx - 2,nums),self.solve(idx - 1,nums))
#         print(list1)
#         return list1[idx]
#
#
# a = Solution()
# q = a.rob(nums1)
# # print("q=",q,a.list1)
# print("q=",q)


# nums1 = [56,95,82,8,45]
# nums1 = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
# nums1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# nums1 = []
# nums1 = [0]

###### 需要考虑数组为空的情况
# class Solution:
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         list1 = [0 for i in range(len(nums))]
#
#         for i in range(len(nums)):
#             list1[i] = max(nums[i] + list1[i - 2],list1[i - 1])
#         return list1[-1]
#
#
#
#
#
# a = Solution()
# q = a.rob(nums1)
# # print("q=",q,a.list1)
# print("q=",q)


# nums1 = [56,95,82,8,45]
# nums1 = [1,2,3,4,5]
# nums1 = []
# class Solution:
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         if nums1 == []:
#             return 0
#         length = len(nums)
#         list1 = [-1 for i in range(length)]
#
#         return self.solve(nums,list1,len(nums)-1)
#
#     def solve(self,nums,list1,idx):
#         if list1[idx] != -1 :
#             return list1[idx]
#         if idx < 0:
#             return 0
#         else :
#             list1[idx] = max(nums[idx] + self.solve(nums,list1,idx-2),self.solve(nums,list1,idx-1))
#             return list1[idx]
#
#
#
#
#
# a = Solution()
# q = a.rob(nums1)
# # print("q=",q,a.list1)
# print("q=",q)
#
# nums1 = [56,95,82,8,45]
# nums1 =[4,1,2,7,5,3,1]
##### 注意 这里没有考虑nums = 1 或者 = 0的情况,懒得写了
# class Solution:
#     def rob(self, nums):
#
#         if nums1 == []:
#             return 0
#         list1 = [-1 for i in range(len(nums))]
#         list1[0] = nums[0]
#         list1[1] = nums[1]
#
#         for idx in range(2,len(nums)):
#             list1[idx] = max(nums[idx] + list1[idx - 2], list1[idx - 1])
#         print("#133,list1",list1[-1])
#         return list1[-1]
#
#
#     def solve(self,nums,list1,idx):
#         if list1[idx] != -1 :
#             return list1[idx]
#         if idx < 0:
#             return 0
#         else :
#             list1[idx] = max(nums[idx] + self.solve(nums,list1,idx-2),self.solve(nums,list1,idx-1))
#             return list1[idx]



# a = Solution()
# q = a.rob(nums1)
# print("q=",q,a.list1)
# print("q=",q)


# --------------------------2019.5.29-------------------------


nums = [56,95,82,8,45]
nums =[4,1,2,7,5,3,1]


class Solution:
    def rob(self, nums: "List[int]") -> int:

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        return dp[-1]



a = Solution()
q = a.rob(nums)
print("q =",q)