#-*- coding:utf-8 -*-
#@Date   : 2019/1/1
#@Author : suyifan
#@File   : 845. Longest Mountain in Array.py


A = [2,1,4,7,3,2,5] # ans = 5
A = [2,2,2] #ans = 0
A = [2,3] # ans = 0
A = [0,1,2,3,4,5,4,3,2,1,0] # ans = 11
A = [875,884,239,731,723,685] # ans = 4
A = [2,3,3,2,0,2] #ans = 0
A = [0,0,1,0,0,1,1,1,1,1] # ans = 3
class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = right = 0
        up = True
        n = len(A)
        # A.append(-9999999999)
        ans = left = right = 0
        for i in range(n-1):
            if (A[i] == A[i + 1]) or ((not up) and A[i] < A[i + 1]):
                if not up:
                    right += 1
                # if not up:
                    ans = max(left + right, ans)
                if A[i] != A[i+1]:
                    left = 1
                else:
                    left = 0
                right = 0
                up = True
            elif up and A[i] < A[i + 1]:
                left += 1
            elif up and A[i] > A[i + 1] and left == 0:
                left = 0
                # continue
            else:
                right += 1
                up = False

        if right != 0 and A[-2]>A[-1]:
            return max(ans,left+right+1)
        else:
            return ans

a = Solution()
q = a.longestMountain(A)
print("q =",q)