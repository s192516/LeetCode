#-*- coding:utf-8 -*-
#@Date   : 2019/1/11
#@Author : suyifan
#@File   : 740. Delete and Earn.py

nums = [2,3,4]

class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        max1 = max(nums)

        # set1 = set(nums)
        # n = len(set1)
        # set_remove = set()
        dp = [0 for i in range(max1+1)]

        dp[1] = dict1.get(1, 0)

        for i in range(2, max1+1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * dict1[i])
        return dp[- 1]

a = Solution()
q = a.deleteAndEarn(nums)
print("q =",q)