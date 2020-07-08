#-*- coding:utf-8 -*-
#@Date   : 2019/1/19
#@Author : suyifan
#@File   : 312. Burst Balloons.py

nums = [3,1,2,4,5,8] # ans = 318

print(3*1*2+3*2*4+3*4*5+3*5*8+1*3*8+1*8*1)
print(3*1*2)

nums = [3,1,5,8] # ans = 167
print(1*5*8+3*1*8   +1*3*8+1*8*1)
print(3*1*5+3*5*8   +1*3*8+1*8*1)
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0
        n = len(nums) - 1
        while nums:
            num = min(nums)
            idx = nums.index(num)

            if idx > 0:
                left = nums[idx - 1]
            else:
                left = 1
            if idx < n:
                right = nums[idx + 1]
            else:
                right = 1
            ans += left * nums[idx] * right
            print(ans)
            nums.remove(num)
            n -= 1
        return ans