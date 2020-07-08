#-*- coding:utf-8 -*-
#@Date   : 2018/10/5
#@Author : suyifan
#@File   : 915. Partition Array into Disjoint Intervals.py


A = [5,0,3,8,6]
A = [1,1,1,12]


class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left = 0
        right = len(A) - 1
        i = left
        j = right
        nums1 = [None for i in range(right + 1)]
        nums2 = [None for i in range(right + 1)]
        min1 = -999999999999
        max1 = 99999999999
        while i <= right:
            temp1 = A[i]
            if temp1 > min1:
                nums1[i] = temp1
                min1 = temp1
            else:
                nums1[i] = min1
            i += 1

            temp2 = A[j]
            if temp2 < max1:
                nums2[j] = temp2
                max1 = temp2
            else:
                nums2[j] = max1
            j -= 1

        print(nums1)
        print(nums2)

        for i in range(right + 1):
            q = nums1[i]
            w = nums2[i]
            print(q - w)

            if nums1[i] < nums2[i+1]:
                return i + 1
print(A)
a = Solution()
q = a.partitionDisjoint(A)
print("q =",q)