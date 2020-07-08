#-*- coding:utf-8 -*-
#@Date   : 2018/12/16
#@Author : suyifan
#@File   : 959. Regions Cut By Slashes.py



grid = ["/\\","\\/"] #答案5
grid = [" /","/ "] # 答案2
# grid = ["\\/","/\\"] #答案4
grid = ["//","/ "] #答案3
grid = ["\\/\\ "," /\\/"," \\/ ","/ / "] #答案3
class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        ans = 1
        n = len(grid)
        m = [ [None] * (n+1) for i in range(n+1)]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == "/" :
                    if (i == 0 or j == n-1  or m[i][j+1]):
                        if j == 0 or m[i+1][j]:
                            ans += 1
                        m[i+1][j] = 1
                    else:
                        m[i+1][j] = 1
                if grid[i][j] == "\\" :
                    if (i == 0 or j == 0 or m[i][j]):
                        if j == n-1 or m[i][j]:
                            ans += 1
                        m[i+1][j+1] = 1
                    else:
                        m[i+1][j+1] = 1
        return ans

a = Solution()
q = a.regionsBySlashes(grid)
print("q =",q)