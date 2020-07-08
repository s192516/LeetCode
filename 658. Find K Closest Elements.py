#-*- coding:utf-8 -*-
#@Date   : 2019/1/2
#@Author : suyifan
#@File   : 658. Find K Closest Elements.py



arr = [0,1,2,4,5]
k = 4
x = 2
arr = [1,2,5,10,13,16,100,100,100]
k = 3
x = 10

arr = [0,1,2,3]
k = 3
x = 2

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        left = 0
        right = len(arr) - k

        while left < right :
            mid = (left+right) // 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left+k]


print(arr)
a = Solution()
q = a.findClosestElements(arr,k,x)
print("q =",q)