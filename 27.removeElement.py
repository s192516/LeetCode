#-*- coding:utf-8 -*-
#@Date   : 2018/9/2
#@Author : huali
#@File   : 27.removeElement.py


nums =[2,2,2,2]
print("原数组:",nums,"len=",len(nums))
val =2
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):

            if nums[i] != val:
                nums[count] =nums[i]
                count +=1


        if count == 0:
            nums.clear()
        return count

a = Solution()
q =a.removeElement(nums,val)

print("返回len:",q)
print("nums=",nums)
for i  in range(q):
    print(nums[i],end=" ")

nums = []
print(nums)


