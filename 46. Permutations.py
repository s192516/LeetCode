#-*- coding:utf-8 -*-
#@Date   : 2018/10/5
#@Author : suyifan
#@File   : 46. Permutations.py


nums = [1,2,2,3]

class Solution:
    def __init__(self):
        self.rtype = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        left = 0
        right = len(nums) - 1
        rtype = []
        return self.solve(nums,rtype, left, right)

    def solve(self, nums,rtype,left, right):
        temp = []
        if left == right:

            rtype.append(nums.copy())
            # print(nums)
            return rtype

        for i in range(left, right + 1):
            if not [nums[i],nums[left]] in temp :####这两行在验证如果有重复的情况
                temp.append([nums[i],nums[left]])#### 实际上是在做47题

                nums[i], nums[left] = nums[left], nums[i]
                self.solve(nums, rtype,left + 1, right)
                nums[i], nums[left] = nums[left], nums[i]

        return rtype

a = Solution()
q = a.permute(nums)
print("q =",q)
print(len( q))

####   1 2 3
####   3 2 1
####   3 1 2
####   3 2 1
####   1 2 3
####   1 3 2



# nums = [1,2,2,3]
# nums = [1,2,3,4]
# nums = "1234"
# nums = "1223"
#
# class Solution:
#     def __init__(self):
#         self.rtype = []
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         rtype = []
#         return self.solve(nums,rtype,0,len(nums) - 1)
#
#
#
#     def solve(self,nums,rtype,left,right):
#         temp = []
#         if left == right :
#
#             rtype.append(nums)
#             return rtype
#
#         for i in range(left,right + 1):
#             if [nums[left],nums[i]] not in temp:
#                 temp.append([nums[left],nums[i]])
#                 nums = self.swap(nums,left,i)
#                 # nums[i] ,nums[left] = nums[left] ,nums[i]
#                 rtype[:] = self.solve(nums,rtype,left + 1,right)
#                 # nums[i],nums[left] = nums[left] ,nums[i]
#                 nums = self.swap(nums,left,i)
#
#         return rtype
#
#     def swap(self,nums,left,i):
#         if left == i:
#             return nums
#         str1 = ""
#         # for q in range(len(nums)):
#         #     if q !=
#         num = nums[:left] + nums[i]+ nums[left + 1:i] + nums[left] + nums[i + 1:]
#         return num
# a = Solution()
# q = a.permute(nums)
# print("q =",q)
# print(len( q))

nums = [1,2,3]

class Solution:
    def __init__(self):
        self.ans = []
    def permute(self, nums):
        left = 0
        right = len(nums) -1
        self.slove(nums,left,right)

        return self.ans

    def slove(self,nums,left,right):
        if left == right:
            self.ans.append(nums[:])
            return

        for i in range(left,right+1):
            nums[left],nums[right] = nums[right],nums[left]
            self.slove(nums,left+1,right)
            nums[left],nums[right] = nums[right],nums[left]



a = Solution()
q = a.permute(nums)
print("q =",q)