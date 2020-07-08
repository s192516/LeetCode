#-*- coding:utf-8 -*-
#@Date   : 2018/12/1
#@Author : suyifan
#@File   : 474 one and zeros.py

strs = ["10", "0001", "111001", "1", "0"]
# strs = ["10", "0001", "1", "0", "111001"]
# strs = ["1","0"]
strs = ["10", "0001", "111001", "1", "0","0101101","10101","101"] # 10,1,0,101,10101

#m 代表0 ,n代表1
m = 6 # 答案5
n = 9
# m = 4 # 答案3
# n = 4

strs = ["10","0001","111001","1","0"] #答案3
m = 4
n = 3
# strs = ["10","0001","111001","1","0"] #答案4
# m = 5
# n = 3
strs = ["0","0","0","0","0","0","0","0","0","0","0","0","0"]
m = 2
n = 2
class Solution:
    # def __init__(self):
    #     self.ans = 0

    def findMaxForm(self, strs, m, n):
        length = len(strs)
        dp = [-1 for _ in range(length)]# * n

        def solve(m,n,left):
            if m < 0 or n < 0 :#or left == length :
                # print(left,"return")
                return -1
            if m >= 0 and n >= 0 and left == length:
                print("yes")
                return 1
            elif left == length:
                print("return")
                return 0

            m0,n1 = self.count(strs[left])
            if dp[left] != -1:
                return dp[left]

            # if m-m0>=0 and n-n1 >=0:
            dp[left] = max(1+solve(m-m0,n-n1,left+1),solve(m,n,left+1))
            # else:
            #     dp[left] = solve(m,n,left+1)
            print(dp)
            return dp[left]

        print(dp)
        return solve(m,n,0)


    def count(self, num):
        m0 = n1 = 0
        for i in num:
            if i == "0":
                m0 += 1
            else:
                n1 += 1
        return m0, n1

print("strs =", strs,m,n)
a = Solution()
q = a.findMaxForm(strs,m,n)
print("q =",q)