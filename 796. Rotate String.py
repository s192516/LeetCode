#-*- coding:utf-8 -*-
#@Date   : 2018/10/15
#@Author : suyifan
#@File   : 796. Rotate String.py




A = "vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg"
B = "fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"


A = "vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg"
B = "fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        len1 = len(A)
        len2 = len(B)
        if len1 != len2:
            return False
        elif len1 == len2 == 0:
            return True

        left1 = left2 = 0

        while left1 < len1:
            while left1 < len1 and A[left1] != B[left2]:
                s = A[left1] ###
                left1 += 1
            if left1 == len1:
                return False
            while left1 < len1 and A[left1] == B[left2]:
                left1 += 1
                left2 += 1
            if left1 != len1:
                return False
        i = 0
        while left2 < len1:
            if A[i] != B[left2]:
                return False
            else:
                i += 1
                left2 += 1
        return True

a = Solution()
q = a.rotateString(A,B)
print("q =",q)