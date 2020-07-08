#-*- coding:utf-8 -*-
#@Date   : 2018/12/21
#@Author : suyifan
#@File   : 406. Queue Reconstruction by Height.py

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        list1 = sorted(people)
        list2 = [None] * len(people)

        print(list1)
        idx = 0
        for i, temp in enumerate(list1):
            # if temp[1] > idx:
            #     list2[temp[1] ] = temp
            # else:
            count = 0
            for j in range(len(list2)):

                if not list2[j] or list2[j][0] == temp[0] :
                    count += 1
                if count == temp[1]+1:
                    list2[j] = temp
                    break
                # idx += 1
        return list2

a = Solution()
q = a.reconstructQueue(people)
print("q =",q)