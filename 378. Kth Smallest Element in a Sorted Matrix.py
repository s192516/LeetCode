#-*- coding:utf-8 -*-
#@Date   : 2018/9/25
#@Author : suyifan
#@File   : 378. Kth Smallest Element in a Sorted Matrix.py


matrix = [[1,2,3],[3,5,6],[7,8,9]]
k = 4
            #.20.25.27.28.29
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
k = 25

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        left = matrix[0][0]
        # left = 0
        right= matrix[-1][-1]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if self.guess(matrix,mid,k):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1

        return ans


    def guess(self,matrix,mid,k):
        """计算mid 是第几个数,以及是否超过k"""
        n = len(matrix)
        left_count = right_count = 0
        for i in range(n):
            # left = matrix[i][0]
            # right = matrix[i][-1]
            left = 0
            right = n - 1
            left_ans = right_ans = -1
            while left <= right:
                guess_mid = (left + right) // 2
                if matrix[i][guess_mid] < mid:
                    left = guess_mid + 1
                    left_ans = guess_mid
                else:
                    right = guess_mid - 1
            left_count += left_ans + 1

            # left = matrix[i][0]
            # right = matrix[i][-1]
            # left = 0
            # right = n - 1
            # while left <= right:
            #     guess_mid = (left + right) // 2
            #     if matrix[i][guess_mid] <= mid:
            #         left += mid + 1
            #         right_ans = guess_mid
            #     else:
            #         right = guess_mid - 1
            # right_count += right_ans + 1

        # if left_ans <= k and right_ans >= k:
        if k > left_count:
            return True
        else:
            return False


a = Solution()
q = a.kthSmallest(matrix,k)
print("q = ",q)
