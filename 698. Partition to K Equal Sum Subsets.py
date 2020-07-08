#-*- coding:utf-8 -*-
#@Date   : 2018/10/29
#@Author : suyifan
#@File   : 698. Partition to K Equal Sum Subsets.py


nums =[10,12,1,2,10,7,5,19,13,1]
k = 4

nums = [4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2]
k = 13

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_all = sum(nums)

        if sum_all % k != 0:
            return False
        average = sum_all // k
        max_num = max(nums)
        if max_num > average:
            return False

        n = len(nums)
        list_idx = [False] * n

        nums.sort(reverse=False)  # 我也是不懂为什么这里写成True结果还能不正确
        print(nums)
        temp = average
        return self.solve(nums, list_idx, n, average, k, temp, 0)

    def solve(self, nums, list_idx, n, average, k, temp, idx):
        print(nums)
        if k == 0:
            return True

        if temp == 0:
            return self.solve(nums, list_idx, n, average, k - 1, average, 0)

        for i in range(idx, n):
            if list_idx[i]:
                continue

            list_idx[i] = True
            if temp - nums[i] >= 0 and self.solve(nums, list_idx, n, average, k, temp - nums[i], idx + 1):
                return True
            list_idx[i] = False

            if temp - nums[i] < 0:
                break

        return False

#         sum1 = average
#         return self.solve(nums,k,list_idx,n,sum1,average,0)

#     def solve(self,nums,k,list_idx,n,sum1,average,idx):
#         if k == 0:
#             return True
#         if sum1 == 0:
#             return self.solve(nums,k-1,list_idx,n,average,average,0)#average

#         for i in range(idx,n):
#             if list_idx[i] :
#                 continue
#             # sum1 += nums[i]
#             list_idx[i] = True
#             if sum1 - nums[i] >= 0 and self.solve(nums,k,list_idx,n,sum1-nums[i],average,idx+1):
#                 return True
#             list_idx[i] = False

#         return False