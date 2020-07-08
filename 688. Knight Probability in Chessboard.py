#-*- coding:utf-8 -*-
#@Date   : 2019/1/2
#@Author : suyifan
#@File   : 688. Knight Probability in Chessboard.py


N,K,r,c = 3,2,0,0 # ans = 0.0625
# N,K,r,c = 3,100,0,0 #
# N,K,r,c = 20,5,0,0 # ans =
N,K,r,c = 20,50,0,0 # ans =

class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        list1 = [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
        if K == 0:
            return 1
        dp = [ [1 for i in range(N)]for j in range(N)]

        for i in range(K):
            temp = [[0 for i in range(N)] for j in range(N)]
            for j in range(N):
                for q in range(N):
                    for arr in list1:
                        a,b = arr[0],arr[1]
                        if 0<=j+a<N and 0<=q+b<N:
                            temp[j+a][q+b] += dp[j][q]
            dp = temp
        return dp[r][c]/ (8**K)


a = Solution()
q = a.knightProbability(N,K,r,c)
print("q =",q)

