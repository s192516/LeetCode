#-*- coding:utf-8 -*-
#@Date   : 2018/9/16
#@Author : suyifan
#@File   : 4. Median of Two Sorted Arrays.py

nums1 = [1,2]
nums2 = [2]

nums2 = [1,2,3,4,5]
nums1 = [1,2,3,6,7,8]

# nums1 = [1,2,3,4,5,99]
# nums2 = [6,7,8,9]
nums1 = [1,2,3,4]
nums2 = [1,2,5,6,7,8]

nums1 = [1,3]
nums2 = [2]

nums1 = [1,2]
nums2 = [3,4]

nums1 = [1]
nums2 = [1]

nums1 = [1,2]
nums2 = [-1,3]
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
    #     """
        # :type nums1: List[int]
        # :type nums2: List[int]
        # :rtype: float
        # """

    # def median(self,A, B):
    #     m, n = len(A), len(B)
    #     if m > n:
    #         A, B, m, n = B, A, n, m
    #     if n == 0:
    #         raise ValueError
    #
    #     imin, imax, half_len = 0, m, (m + n + 1) // 2
    #     while imin <= imax:
    #         i = (imin + imax) // 2
    #         j = half_len - i
    #         if i < m and B[j - 1] > A[i]:
    #             # i is too small, must increase it
    #             imin = i + 1
    #         elif i > 0 and A[i - 1] > B[j]:
    #             # i is too big, must decrease it
    #             imax = i - 1
    #         else:
    #             # i is perfect
    #
    #             if i == 0:
    #                 max_of_left = B[j - 1]
    #             elif j == 0:
    #                 max_of_left = A[i - 1]
    #             else:
    #                 max_of_left = max(A[i - 1], B[j - 1])
    #
    #             if (m + n) % 2 == 1:
    #                 return max_of_left
    #
    #             if i == m:
    #                 min_of_right = B[j]
    #             elif j == n:
    #                 min_of_right = A[i]
    #             else:
    #                 min_of_right = min(A[i], B[j])
    #
    #             return (max_of_left + min_of_right) / 2.0








        if  len(nums1)  > len(nums2):
            nums1[:],nums2[:] = nums2[:],nums1[:]
        len1 = nums1.__len__()
        len2 = nums2.__len__()
        min1 = 0
        max1 = len1
        half_len = (len1 + len2 + 1) // 2

        # print("nums1 = ",nums1,)
        # print("nums2 = ",nums2)
        # if len1 == 0:
        #     return None
        if len2 == 0:
            return 0.0
        if len1 == 0:
            if len2 % 2 == 0:
                return (nums2[len2//2 -1] + nums2[len2 // 2] ) / 2
        while min1 <= max1:
            i = (min1 + max1) // 2
            j = half_len - i
            if i < len1 and nums2[j - 1] > nums1[i]:
                min1 = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                max1 = i - 1
                # i = (min1 + max1) // 2
                # j = (max1 + max2 + 1) // 2 - i

                # i = (min1 + max1) // 2
                # j = (max1 + max2 + 1) // 2 - i
            else:
                if i == 0:
                    rtype_left = nums2[j-1]
                elif j == 0 :
                    rtype_left = nums1[i -1]
                else:
                    rtype_left = max(nums1[i - 1], nums2[j - 1])

                if (len1 + len2) % 2 == 1:
                    return rtype_left
                else:
                    if i == len1:
                        rtype_right = nums2[j]
                    elif j == len2:
                        rtype_right = nums1[i]
                    else:
                        rtype_right = min(nums1[i], nums2[j])
                    return (rtype_left + rtype_right) / 2

                    # print("i=",i,"j=",j,nums1[i-1],nums2[j])
                    # print(max(nums1[i-1],nums2[j-1]) , min(nums1[i],nums2[j]))
                    # return (2 + 3) / 2
                    # return (max(nums1[i - 1], nums2[j - 1]) + min(nums1[i], nums2[j])) / 2

print(nums1)
print(nums2)
a = Solution()
q = a.findMedianSortedArrays(nums1,nums2)
print("q=",q)

# A = [1,3]
# B = [2]
# a = Solution()
# q = a.median(A,B)
# print("q =",q)