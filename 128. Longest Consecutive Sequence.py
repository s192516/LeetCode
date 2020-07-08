#-*- coding:utf-8 -*-
#@Date   : 2018/11/26
#@Author : suyifan
#@File   : 128. Longest Consecutive Sequence.py


nums = [100,4,200,1,3,2]


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set(nums)
        ans = 0
        # while set1:
        for num in nums:
            n = 0
            while num in set1:
                # if num in set1:
                n += 1
                set1.remove(num)
                up = num + 1
                down = num - 1
                while up in set1:
                    n += 1
                    set1.remove(up)
                    up += 1
                while down in set1:
                    n += 1
                    set1.remove(down)
                    down -= 1
                ans = max(n,ans)
        return ans

a = Solution()
q = a.longestConsecutive(nums)
print("q =",q)