#-*- coding:utf-8 -*-
#@Date   : 2018/10/26
#@Author : suyifan
#@File   : 213. House Robber II.py


nums = [4,1,2,7,5,3,1]
nums = [2,3,2]

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        rtype1 = [0 for _ in range(n - 1)]

        rtype1[0] = nums[0]
        rtype1[1] = max(nums[1], nums[0])
        for i in range(2,n - 1):
            rtype1[i] = max((nums[i] + rtype1[i - 2]), rtype1[i - 1])
        max1 = rtype1[-1]
        print(rtype1)
        rtype2 = [0 for _ in range(n)]
        # rtype2[0] = 0
        rtype2[1] = nums[1]

        for i in range(2, n):
            if i == 2:
                rtype2[2] = max(rtype2[1], nums[2])
            rtype2[i] = max((nums[i] + rtype2[i - 2]), rtype2[i - 1])
        max2 = rtype2[-1]
        print(max1, max2)
        return max(max1, max2)
print("nums =",nums)
a = Solution()
q = a.rob(nums)
print("q =",q)