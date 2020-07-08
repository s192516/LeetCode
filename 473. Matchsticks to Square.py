#-*- coding:utf-8 -*-
#@Date   : 2018/12/16
#@Author : suyifan
#@File   : 473. Matchsticks to Square.py


nums = [1,1,2,2,2]
nums = [3,3,3,3,4]
nums = [5,5,5,5,4,4,4,4,3,3,3,3]
nums = [10,6,5,5,5,3,3,3,2,2,2,2]
nums = [7,1,13,6,19,18,12,3,15,4,20,11,2,15,14]


class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:
            return False

        sum1 = sum(nums)
        if sum1 % 4 != 0:
            return False
        count = sum1 // 4
        max1 = max(nums)
        if max1 > count:
            return False
        nums.sort(reverse=True)
        n = len(nums)

        dp = [0] * 4

        def dfs(idx):
            if idx == n:
                return dp[0] == dp[1] == dp[2] == count

            for i in range(4):
                if dp[i] + nums[idx] <= count:
                    dp[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    dp[i] -= nums[idx]
            return False

        return dfs(0)

a = Solution()
q = a.makesquare(nums)
print("q =",q)