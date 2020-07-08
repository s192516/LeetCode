#-*- coding:utf-8 -*-
#@Date   : 2018/9/9
#@Author : suyifan
#@File   : 219. Contains Duplicate II.py

# nums = [1,2,3,4,1]
# k = 4

# nums = [1,0,1,1]
# k = 1

nums = [99,99]
k = 2

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict1 = {}

        for i in range(len(nums)):
            if nums[i] in dict1:
                max_k = i - dict1[nums[i]]
                if max_k <= k:
                    return True
                else:
                    dict1[nums[i]] = i
            else:
                dict1[nums[i]] = i
        return False




a = Solution()
q = a.containsNearbyDuplicate(nums,k)
print("q= ",q)