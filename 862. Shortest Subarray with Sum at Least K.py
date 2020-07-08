#-*- coding:utf-8 -*-
#@Date   : 2019/1/4
#@Author : suyifan
#@File   : 862. Shortest Subarray with Sum at Least K.py

# A = [2,-1,2]
# K = 3
# A = [1,2]
# K = 4
# A = [1]
# K = 1
# A = [48,99,37,4,-31]
# K = 140 # ans = 2
# A = [84,-37,32,40,95]
# K = 167 # ans = 3
# A = [56,-21,56,35,-9]
# K = 61 # ans = 2


# -----------------------用优先队列的正确版本-------------------
# class Solution:
#     def shortestSubarray(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: int
#         """
#         n = max(A)
#         if n >= K:
#             return 1
#
#         n = len(A)
#         dp = [0] * (n+1)
#         for i,num in enumerate(A):
#             dp[i+1] = dp[i] + num
#
#
#         queue = []
#         res = 1e15
#         for i in range(n,-1,-1):
#             while queue and queue[0] -i > res :
#                 queue.pop(0)
#             while queue and dp[queue[-1]] <= dp[i]:
#                 queue.pop()
#             queue.append(i)
#             if dp[queue[0]] >= dp[i] + K:
#                 cur = self.solve(queue,i,dp,K)
#                 res = min(cur,res)
#         return res if res != 1e15 else -1
#
#     def solve(self,queue,i,dp,k):
#         down = 0
#         up = len(queue) - 1
#         # mid = 0
#         j = 1e15
#         while up >= down:
#             mid = (up+down)>>1
#             if dp[queue[mid]] >= dp[i] +k:
#                 j = queue[mid]
#                 down = mid + 1
#             else:
#                 up = mid - 1
#
#         return j-i  if j != 1e15 else 1e15



# a = Solution()
# q = a.shortestSubarray(A,K)
# print("q =",q)



#-----------------------------草稿---------------
A = [2,-1,2]
K = 3
# A = [1,2]
# K = 4
# A = [1]
# K = 1
# A = [48,99,37,4,-31]
# K = 140 # ans = 2
# A = [84,-37,32,40,95]
# K = 167 # ans = 3
# A = [56,-21,56,35,-9]
# K = 61 # ans = 2
A = [-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
K = 151 # ans = 2

class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = max(A)
        if n >= K:
            return 1
        n = len(A)
        sum_a = [0] * (n+1)
        for i in range(1,n+1):
            sum_a[i] = sum_a[i-1] + A[i-1]


        list_idx = []
        ans = 1e15
        for i,num in enumerate(sum_a):
            while list_idx and num - sum_a[list_idx[0]] >= K:
                ans = min(ans,i-list_idx.pop(0))
            while list_idx and num <= sum_a[list_idx[-1]]:
                list_idx.pop()
            list_idx.append(i)

        return ans if ans != 1e15 else -1


#-----------------------排名第一的答案
# class Solution:
#     def shortestSubarray(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: int
#         """
#         import collections
#         import itertools
#
#         asum = [0] + list(itertools.accumulate(A))
#         cds = collections.deque()
#         ans = float('inf')
#         for i, num in enumerate(asum):
#             while cds and num - asum[cds[0]] >= K:
#                 ans = min(ans, i - cds.popleft())
#             while cds and num <= asum[cds[-1]]:
#                 cds.pop()
#             cds.append(i)
#         return ans if ans < float('inf') else -1
a = Solution()
q = a.shortestSubarray(A,K)
print("q =",q)