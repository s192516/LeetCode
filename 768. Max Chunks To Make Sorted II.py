#-*- coding:utf-8 -*-
#@Date   : 2018/12/19
#@Author : suyifan
#@File   : 768. Max Chunks To Make Sorted II.py



arr = [2,1,3,4,4] # 答案4
arr = [1,1,0,0,1] # 答案2
arr = [5,4,3,2,1] # 答案1
arr = [1,1,1,1,1] # 答案5
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        stack = []
        n = arr[0]
        for num in arr:
            if num > n:
                stack.append(num)
                n = num
            else:
                stack.append(n)

        n = arr[-1]
        stack1 = []
        for num in reversed(arr):
            if num < n:
                stack1.insert(0,num)
                n = num
            else:
                stack1.insert(0,n)

        ans = 1
        for i in range(len(arr)-1):
            if stack[i] <= stack1[i+1]:
                ans += 1
        # print(stack)
        # print(stack1)
        return ans

a = Solution()
q = a.maxChunksToSorted(arr)
print("q =",q)