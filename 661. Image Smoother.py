#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 661. Image Smoother.py

# M = [[1,1,1],[1,0,1],[1,1,1]]
# # M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
# # M = [[1]]
# # # M = [[1,2]]
# # # M = [[1],[2]]
# # # M = [[1,2],[3,4]]
# #
# #
# # class Solution:
# #     def imageSmoother(self, M):
# #         """
# #         :type M: List[List[int]]
# #         :rtype: List[List[int]]
# #         """
# #         n = len(M)
# #         m = len(M[0])
# #         rtype = [[0]*m for i in range(n)]
# #         n -= 1
# #         m -= 1
# #         rtype[0][0] = int((M[0][0]+M[0][1]+M[1][0]+M[1][1])//4)
# #         rtype[0][m] = int((M[0][m-1]+M[0][m]+M[1][m-1]+M[1][m])//4)
# #         rtype[n][0] = int((M[n-1][0]+M[n-1][1]+M[n][0]+M[n][1])//4)
# #         rtype[n][m] = int((M[n-1][m-1]+M[n-1][m]+M[n][m-1]+M[n][m])/4)
# #
# #         for i in range(1,m):
# #             rtype[0][i] = int((M[0][i-1]+M[0][i]+M[0][i+1]+M[1][i-1]+M[1][i]+M[1][i+1])//6)
# #         for i in range(1,m):
# #             rtype[n][i] = int((M[n-1][i-1]+M[n-1][i]+M[n-1][i+1]+M[n][i-1]+M[n][i]+M[n][i+1])//6)
# #         for i in range(1,n):
# #             rtype[i][0] = int((M[i-1][0]+M[i][0]+M[i+1][0]+M[i-1][1]+M[i][1]+M[i+1][1])//6)
# #         for i in range(1,n):
# #             rtype[i][m] = int((M[i-1][m-1]+M[i][m-1]+M[i+1][m-1]+M[i-1][m]+M[i][m]+M[i+1][m])//6)
# #
# #
# #         for i in range(1,n):
# #             for j in range(1,m):
# #                 rtype[i][j] = int((M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j-1]+M[i][j]+M[i][j+1]+M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])//9)
# #
# #         return  rtype
# #
# #
# # a = Solution()
# # q = a.imageSmoother(M)
# # print("q=",q)



M = [[1,1,1],[1,0,1],[1,1,1]]
M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
# M = [[1]]
# M = [[1,2]]
# M = [[1],[2]]
# M = [[1,2],[3,4]]


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(M)
        m = len(M[0])
        rtype = [[0]*m for i in range(n)]
        # n -= 1
        # m -= 1
        for i in range(n):
            for j in range(m):
                sum = 0
                count = 0
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if ii>=0 and ii < n and jj >=0 and jj < m:
                            sum +=M[ii][jj]
                            count +=1
                rtype[i][j] = sum//count


        # for i in range(1,n):
        #     for j in range(1,m):
        #         rtype[i][j] = int((M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j-1]+M[i][j]+M[i][j+1]+M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])//9)

        return  rtype


a = Solution()
q = a.imageSmoother(M)
print("q=",q)