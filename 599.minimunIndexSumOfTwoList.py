#-*- coding:utf-8 -*-
#@Date   : 2018/9/5
#@Author : huali
#@File   : 599.minimunIndexSumOfTwoList.py

list1 = ["a","b","Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["b","a","Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]




class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        rtype = []
        target = 10000
        for i in range(len(list1)):
            dict1[list1[i]] = i+1

        for i in range(len(list2)):
            if list2[i] in dict1:
                temp = dict1[list2[i]] + (i + 1)
                if temp < target:
                    target = temp
                    rtype = [list2[i]]
                elif temp == target :
                    rtype.append(list2[i])

        return rtype





a = Solution()
q = a.findRestaurant(list1,list2)
print("q=",q)