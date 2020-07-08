#-*- coding:utf-8 -*-
#@Date   : 2018/11/9
#@Author : suyifan
#@File   : 324. Wiggle Sort II.py

nums = [1, 5, 1, 1, 6, 4,7]
nums = [1,1,2,1,2,2,1]
nums = [1,5,1,1,6,4]
nums = [5,1]
nums = [4,5,6,5]
nums = [1]
nums = [5,3,1,2,6,7,8,5,5]
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse = True)
        right = len(nums)
        mid = (right) // 2
        # print(nums)
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        # print(nums1,"1")
        # print(nums2,"2")
        for i in range(mid):
            nums[i*2] = nums2[i]
            nums[i*2+1] = nums1[i]
        if len(nums2) > len(nums1):
            nums[-1] = nums2[-1]

print(nums)
a = Solution()
q = a.wiggleSort(nums)
print(nums)

#This post is mainly about what I call "virtual indexing" technique (I'm sure I'm not the first who came up with this, but I couldn't find anything about it, so I made up a name as well. If you know better, let me know).

#First I find a median using nth_element. That only guarantees O(n) average time complexity and I don't know about space complexity. I might write this myself using O(n) time and O(1) space, but that's not what I want to show here.

#This post is about what comes after that. We can use three-way partitioning to arrange the numbers so that those larger than the median come first, then those equal to the median come next, and then those smaller than the median come last.

#Ordinarily, you'd then use one more phase to bring the numbers to their final positions to reach the overall wiggle-property. But I don't know a nice O(1) space way for this. Instead, I embed this right into the partitioning algorithm. That algorithm simply works with indexes 0 to n-1 as usual, but sneaky as I am, I rewire those indexes where I want the numbers to actually end up. The partitioning-algorithm doesn't even know that I'm doing that, it just works like normal (it just uses A(x) instead of nums[x]).

#Let's say nums is [10,11,...,19]. Then after nth_element and ordinary partitioning, we might have this (15 is my median):