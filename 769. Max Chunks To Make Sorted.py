#-*- coding:utf-8 -*-
#@Date   : 2018/12/19
#@Author : suyifan
#@File   : 769. Max Chunks To Make Sorted.py



arr = [1,0,2,3,4]


class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nums = sorted(arr)

        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[num] = i

        cur = 0
        ans = 1
        for i in range(len(arr)):
            cur = max(nums.index(arr[i]), i)
            if num_dict[arr[i]] > cur:
                ans += 1
        return ans

a = Solution()
q = a.maxChunksToSorted(arr)
print("q =",q)