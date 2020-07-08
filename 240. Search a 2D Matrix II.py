#-*- coding:utf-8 -*-
#@Date   : 2018/11/8
#@Author : suyifan
#@File   : 240. Search a 2D Matrix II.py


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        height = len(matrix)
        width = len(matrix[0])
        if height * width == 0:
            return False

        row = self.help1(matrix, 0, height, target)
        column = self.help2(matrix, row, 0, width, target)
        if column == -1:
            return False
        else:
            return True

    def help1(self, matrix, up, down, target):
        while up < down:
            mid = (up + down) // 2
            if matrix[mid][0] < target:
                up = mid + 1
                ans = mid
            # elif martix[mid][0] == target:
            else:
                down = mid - 1
        print("111,row =",ans)
        return ans - 1

    def help2(self, matrix, row, left, right, target):
        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
                ans = mid
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return mid
        print("222,column =",mid)
        return -1

print(matrix)
a = Solution()
q = a.searchMatrix(matrix,target)
print("q =",q)