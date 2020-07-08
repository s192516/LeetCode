#-*- coding:utf-8 -*-
#@Date   : 2018/9/27
#@Author : suyifan
#@File   : 593. Valid Square.py

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

# p1 = [0,0]
# p2 = [1,1]
# p3 = [1,0]
# p4 = [0,1]
p1 = [0,0]
p2 = [1,0]
p3 = [0,1]
p4 = [0,0]

p1 = [1,0]
p2 = [0,1]
p3 = [-1,0]
p4 = [0,-1]

p1 = [1,1]
p2 = [5,3]
p3 = [3,5]
p4 = [7,7]

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # 先判断四条边是否相等
        list1 = self.vector(p1,p2)#向量a->b,即向量1
        list2 = self.vector(p1,p3)#向量a->c,向量2
        side1 = self.length(list1)
        side2 = self.length(list2)
        if p1 == p4 :
            return False

        if side1 == side2:#判断a到b的距离等于a到c
            return self.solve(p1,p2,p3,p4)

        elif side1 > side2:
            return self.solve(p1,p4,p3,p2)

        elif side1 < side2:
            return self.solve(p1,p2,p4,p3)

    def solve(self,p1,p2,p3,p4):

        list1 = self.vector(p1, p2)
        side1 = self.length(list1)

        # list2 = self.vector(p1, p3)
        # side2 = self.length(list2)

        list3 = self.vector(p4, p2)  # 向量d->b,向量3
        side3 = self.length(list3)

        list4 = self.vector(p4, p3)  # 向量d->c,向量4
        side4 = self.length(list4)
        if side3 == side4 and side1 == side3:  # 判断四条边是否长度相等
            return self.vertical(list1,list3)

        else:
            return False

    def vertical(self,list1,list3):
        if list1[0] * list3[0] + list1[1] * list3[1] == 0:
            return True
        else:
            return False

    def vector(self,p1,p2):
        #计算p1到p2的长度
        return [p2[0] - p1[0],p2[1] - p1[1]]

    def length(self,l1):
        return l1[0] ** 2 + l1[1] ** 2





a = Solution()
q = a.validSquare(p1,p2,p3,p4)
print("q = ",q)