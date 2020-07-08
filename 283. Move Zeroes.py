#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 283. Move Zeroes.py



#####这种方法吧,可以是可以,但总是觉得不太好,pop和append都是语法糖

nums1 = [0,1,2,3,0]
nums1 = [0,0,1]
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #######
        # length = len(nums)
        # i = 0
        # while i < length:
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #         length -= 1
        #     else:
        #         i += 1
        # print(nums)




# a = Solution()
# q = a.moveZeroes(nums1)
# print(nums1)


nums1 = [0,1,2,3,0]
# nums1 = [0,0,1,0,0]
# nums1 = [0,0,1]
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j = 0,len(nums) -1
        while i < j:
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            elif nums[j] == 0:
                j -= 1
                k = i + 1
                while k < j:
                    if nums[k] != 0:
                        nums[i],nums[k] = nums[k],nums[i]
                        break

                    else:
                        k += 1
                i = k


a = Solution()
q = a.moveZeroes(nums1)
print(nums1)