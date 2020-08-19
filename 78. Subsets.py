#-*- coding:utf-8 -*-
#@Date   : 2018/10/5
#@Author : suyifan
#@File   : 78. Subsets.py


nums = [1,2,3]

'''
class Solution:
    def __init__(self):
        self.rtype = []
        self.i = 0

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        left = 0
        right = len(nums) - 1
        rtype = []
        i = 0
        return self.solve(nums, rtype, left, right,i)

    def solve(self, nums, rtype, left, right,i):

        if left == right:
            rtype.append(nums[i:])
            # print(nums)
            return rtype
        i += 1
        # print("i=" ,i,end="   ")
        self.i += 1
        # print("self =",self.i)
        for i in range(left,right+1):

            nums[i], nums[left] = nums[left], nums[i]
            # if left == right:
            # rtype.append(nums[left:])
            self.solve(nums, rtype, left + 1, right,i)
            # rtype.append(nums[i:])

            nums[i], nums[left] = nums[left], nums[i]


        return rtype

    def fun1(self,nums,rtype,left,right):
        rtype.append(nums[left:right + 1])
        return rtype


a = Solution()
q = a.subsets(nums)
print("q =",q)

'''

'''
# [[1], [2], [3], [3, 2],[2, 1],[3, 1], [3, 2, 1],
#  [2],  [1], [3],  [1],[2], [1], [1, 2], [2]]

nums = [1,2,3]
class Solution:
    def subsets(self, nums):
        ans = [[]]
        for line in nums:
            for j in ans[:]:
                ans.append(j+[line])
        return ans


a = Solution()
q = a.subsets(nums)
print("q =",q)
'''


''''''


class Solution:
    def subsets(self, nums) :
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


''''''