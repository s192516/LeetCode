#-*- coding:utf-8 -*-
#@Date   : 2018/9/4
#@Author : huali
#@File   : 88.mergeSortedArray.py

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
def me(nums1):
    m =0
    for i in range(len(nums1)):

        if nums1[i] != 0:
            m =i
        else :
            break
    return m+1
m = me(nums1)

n = len(nums2)
print("m=",m,n)
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index_1,index_2 = 0,0
        rtype = []
        for i  in range(m+n):
            if index_1 >= m:
                rtype.append(nums2[index_2])
                index_2 += 1
            elif index_2 >= n:
                rtype.append(nums1[index_1])
                index_1 += 1

            elif nums1[index_1] > nums2[index_2]:
                rtype.append(nums2[index_2])
                index_2 += 1
            else :
                rtype.append(nums1[index_1])
                index_1 += 1
            # print(rtype)
        nums1 = rtype
        return nums1

a = Solution()
q = a.merge(nums1,m,nums2,n)
print("q=",q)