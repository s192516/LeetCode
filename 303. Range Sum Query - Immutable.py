#-*- coding:utf-8 -*-
#@Date   : 2018/9/21
#@Author : suyifan
#@File   : 303. Range Sum Query - Immutable.py

["NumArray","sumRange","sumRange","sumRange"]
nums = [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

nums = [1,2,3,4,5]
i = 1
j = 4

nums = [-2,0,3,-5,2,-1]
i = 0
j = 2

# i = 2
# j = 5

# i = 0
# j = 5

#### 看懂题目给的那个list,其实也没那么可怕,就是一个num,以及n组,i,j
#### sum(i,j) = sum(0,j) - sum(0,i-1)
#### 注意!!!当j= 0 时候 需要返回 sum(0) 也就是说nums[0]
#### sum(n) 可以用动态规划(或者首都算不上动态规划,直接一个for循环加上去就可以)
#### 但是for循环需要注意初始化情况,动态规划省事一点

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.list1 = [0 for q in range(len(nums))]
        idx = len(self.list1)-1
        self.found_list(nums,idx)
        print(self.list1)

    def found_list(self,nums,idx):
        if idx < 0:
            return 0

        if self.list1[idx] != 0 :
            return self.list1[idx]
        else:
            self.list1[idx] = self.found_list(nums,idx-1) + nums[idx]
            return self.list1[idx]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i >0:
            return self.list1[j] - self.list1[i-1]
        else:
            return self.list1[j]

a = NumArray(nums)
q = a.sumRange(i,j)
print("q=",q)
