#-*- coding:utf-8 -*-
#@Date   : 2018/11/11
#@Author : suyifan
#@File   : 300. Longest Increasing Subsequence.py



nums = [2,2,2,2,10,9,2,5,3,7,101,18]
nums = [2,2,2,2,10,9,-1,5,3,7,101,18]

# nums = [2,10,9,2,5,3,7,101,18,1,100]


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0]=nums[0]
        rtype = 1
        for i in range(n):
            if nums[i] > dp[rtype-1]:
                dp[rtype] = nums[i]
                rtype += 1
                # print(dp)
            else:
                left,right = 0,rtype

                while left < right:

                    mid = (left+right) // 2

                    # if i == 10:
                    #     print(left,right,mid)
                    # if mid == 0 and dp[0] > nums[i]:
                    #     dp[0] = nums[i]
                    #     break
                    if (nums[i] > dp[mid-1] and nums[i]<dp[mid]) or nums[i]==dp[mid]:
                        dp[mid] = nums[i]
                        break
                    elif nums[i] > dp[mid]:
                        left = mid + 1

                    elif nums[i] < dp[mid]:
                        right = mid - 1
                if left == right:
                    # print(i,nums[i],dp)
                    dp[left] = nums[i]

        # print(dp)
        return rtype

a = Solution()
q = a.lengthOfLIS(nums)
print("q =",q)
