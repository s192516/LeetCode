#-*- coding:utf-8 -*-
#@Date   : 2018/11/25
#@Author : suyifan
#@File   : 51. N-Queens.py


n = 4

#### 正确解法1
# class Solution:
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         res = []
#         if n <= 0:
#             return res
#         self.helper(res,[0]*n,0)
#         return res
#
#
#
#     def helper(self,res,queens,pos):
#         if pos == len(queens):
#             self.add_solution(res,queens)
#             return res
#
#         for i in range(len(queens)):
#             queens[pos] = i
#             if (self.is_valid(queens,pos)):
#                 self.helper(res,queens,pos+1)
#         return res
#
#     def is_valid(self,queens,pos):
#         for i in range(pos):
#             if queens[i] == queens[pos]:
#                 return False
#             elif abs(queens[pos] - queens[i]) == abs(i-pos):
#                 return False
#         return True
#
#     def add_solution(self,res,queens):
#         n = len(queens)
#         list1 = []
#         for i in range(len(queens)):
#             array = ["."] * n
#             for j in range(len(queens)):
#                 if queens[i] == j:
#                     array[j] = "Q"
#             str1 = "".join(array)
#
#             list1.append(str1)
#         res.append(list1)
#         # return res
#
#
#
#
#
#
# a = Solution()
# q = a.solveNQueens(n)
# print("q =",q)


### 练习
n = 4
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        res = []
        if  self.n <= 0:
            return res
        queens = [0] * self.n
        pos = 0
        self.helper(res,queens,pos)
        return res

    def helper(self,res,queens,pos):
        if pos == self.n:
            self.add_solution(res,queens)
            return

        for i in range(self.n):
            queens[pos] = i
            if self.is_valid(queens,pos):
                self.helper(res,queens,pos+1)
        return res

    def is_valid(self,queens,pos):
        for i in range(pos):
            if queens[i] == queens[pos]:
                return False
            elif abs(queens[i] - queens[pos]) == abs(i-pos):
                return False
        return True


    def add_solution(self,res,queens):
        list1 = []
        for i in range(self.n):
            array = ["."] * self.n
            array[queens[i]] = "Q"
            str1 = "".join(array)
            list1.append(str1)
        res.append(list1)
        return res


a = Solution()
q = a.solveNQueens(n)
print("q =",q)