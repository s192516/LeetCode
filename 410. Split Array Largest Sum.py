#-*- coding:utf-8 -*-
#@Date   : 2018/9/25
#@Author : suyifan
#@File   : 410. Split Array Largest Sum.py

nums = [1,2,3,4,5]
n = 2

nums = [7,2,5,10,8]
m = 2

nums = [1,2147483647]
n = 2

nums = [1,5]
n = 2

print(nums)
class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left = 0
        right = 1
        ans = 0
        # mid = 0
        for i in nums:
            right += i
        while left < right:
            mid = (left + right) // 2

            if self.guess(mid,nums,m):
                right = mid
                ans = mid
            else:
                left = mid + 1
                # ans = mid

        return ans

    def guess(self,mid,nums,m):
        sum = 0
        for i in nums:
            if sum + i > mid:
                m -= 1
                sum = i
                if i > mid:
                    return False
            else:
                sum += i

        if m >= 1:
            return True
        else:
            return False

a = Solution()
q = a.splitArray(nums,n)
print("q=",q)