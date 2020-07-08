#-*- coding:utf-8 -*-
#@Date   : 2018/11/8
#@Author : suyifan
#@File   : 275. H-Index II.py


nums = [0,1,3,5,6] #正确 3
nums = [0,1,3,5,6,8,13,823,45645,1236756] # 正确6
nums = [0]
nums = [1]
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0

        left = 0
        right = n
        ans = 0
        while left < right:
            mid = (left + right) // 2
            if self.solve(n,mid,nums):
                left = mid + 1
                # ans = n - mid
            else:
                right = mid
                ans = n - mid
                # ans = mid
        return ans

    def solve(self,n,mid,nums):
        if n-mid <= nums[mid]:
            return False
        else:
            return True





a = Solution()
q = a.hIndex(nums)
print("q =",q)