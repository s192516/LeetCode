#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 189. Rotate Array.py

nums = [1,2,3,4,5]
k = 1
nums = [1,2,3,4,5,6,7]
k = 3

nums = [1]
k = 5

nums = [-1,-100,3,99]
k = 2

nums = [1,2]
k = 3


nums = [1,2,3,4,5,6,7]
k = 3

nums = [1,2]
k = 0
##### 考虑移动次数超过数组长度的情况
class Solution:
    def rotate(self, nums, k):
        # nums = ["a","b","c"]
            # k = len(nums) - k % len(nums)
            # nums[:] = nums[k:] + nums[0:k]
        i = len(nums)
        k = k % i
        # if k != 0:
        self.reverse(nums, 0, i - k - 1)
        self.reverse(nums, i - k, i - 1)
        self.reverse(nums, 0, i - 1)


    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

a = Solution()
q = a.rotate(nums,k)
print(nums)