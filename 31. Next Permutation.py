#-*- coding:utf-8 -*-
#@Date   : 2018/10/5
#@Author : suyifan
#@File   : 31. Next Permutation.py


nums = [1,2,3]
nums = [1,3,2]
nums = [2,1,3]
nums = [2,3,1]
nums = [3,1,2]
nums = [3,2,1]
nums = [1,1]
nums = [5,1,1]

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        right = len(nums) - 1
        exchange = False
        idx = -1
        for i in range(right - 1, -1, -1):
            if nums[i] >= nums[i + 1]:
                # idx = i
                pass
            else:
                exchange = True
                idx = i
                break

        if exchange:
            # print("NUMS= ",nums, idx)

            for i in range(right ,-1, -1):
                if nums[idx] < nums[i]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    # print("i,idx",i,idx)
                    left = idx + 1
                    # break

                # print("nums ====",nums)
                    while left < right:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
                        right -= 1
                    break
        else:
            nums.sort()

print("initial =",nums)
a = Solution()
q = a.nextPermutation(nums)
print("q =",nums)





