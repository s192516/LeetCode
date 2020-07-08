#-*- coding:utf-8 -*-
#@Date   : 2018/11/6
#@Author : suyifan
#@File   : 179. Largest Number.py

nums = [3,30,34,5,9]
nums = [74,21,33,51,77,51,90,60,5,56]


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        nums = [str(i) for i in nums]
        # nums.sort(reverse = True)
        n = len(nums)
        for q in range(n - 1):
            for i in range(q, n - 1):
                if nums[i] + nums[i + 1] < nums[i + 1] + nums[i]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        rtype = "".join(nums)
        if rtype[0] == "0":
            rtype = "0"

        return rtype


a = Solution()
q = a.largestNumber(nums)
print("q =",q)