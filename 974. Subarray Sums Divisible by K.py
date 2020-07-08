#-*- coding:utf-8 -*-
#@Date   : 2019/1/6
#@Author : suyifan
#@File   : test_3.py

A = [4,5,0,-2,-3,1]
K = 5 # ans = [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        dp = [0] * n
        for i,num in enumerate(A):
            if i != 0:
                dp[i] = (dp[i-1] + num) % K
            else:
                dp[i] = num % K
        ans = 0
        dict1 = {}
        for i in dp:
            dict1[i] = dict1.get(i,0)+1
        print(dict1)
        for k,v in dict1.items():
            if k != 0:
                ans += v*(v-1)//2
            else:
                ans += v*(v+1)//2
        return ans


        # for i in range(n):
        #     if dp[i] == 0:
                # print("yes")
                # ans.append(A[:i + 1])
                # ans += 1
            # for j in range(i+1,n):
            #     if dp[i] == dp[j]:
            #         ans += 1
                #     ans.append(A[i+1:j+1])
        # print(dp)
        return ans

        # print(dp)
        # print(ans)

        # print(%5)


a = Solution()
q = a.subarraysDivByK(A,K)
print("q =",q)