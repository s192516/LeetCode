#-*- coding:utf-8 -*-
#@Date   : 2018/9/2
#@Author : huali
#@File   : 26.removeDuplicatesFromSortedArray.py

#删除排序数组中的重复项

nums =[0,0,1,1,1,2,2,3,3,4]
print("原数组:",nums)
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i in range(1,len(nums)):

            if nums[i] != nums[count]:
                count +=1
                nums[count] =nums[i]
        if len(nums) != 0:
            count +=1
        return count


a = Solution()
q =a.removeDuplicates(nums)

print()
print("返回:",q)
print("nums=",nums)
for i  in range(q):
    print(nums[i],end=" ")