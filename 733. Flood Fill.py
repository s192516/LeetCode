#-*- coding:utf-8 -*-
#@Date   : 2019/1/18
#@Author : suyifan
#@File   : 733. Flood Fill.py


image = [[1,1,1],[1,1,0],[1,0,1]]
sr,sc,newColor = 1,1,2


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        num = image[sr][sc]
        set1 = ((0,1),(0,-1),(1,0),(-1,0))
        set2 = set()
        set2.add((sr,sc))
        set3 = set()
        set3.add((sr,sc))
        # print(set3)
        m = len(image)
        n = len(image[0])
        while set2:
            i,j = set2.pop()
            for q,w in set1:
                a,b = i+q,j+w
                if 0<= a < m and 0<= b< n :
                    if (a,b) not in set3 and image[a][b] == num:
                        set3.add((a,b))
                        set2.add((a,b))
        # print(set3)
        for i,j in set3:
            image[i][j] = newColor
        return image


a = Solution()
q = a.floodFill(image,sr,sc,newColor)
print("q=",q)