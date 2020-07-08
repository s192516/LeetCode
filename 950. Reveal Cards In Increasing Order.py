#-*- coding:utf-8 -*-
#@Date   : 2018/11/25
#@Author : suyifan
#@File   : 950. Reveal Cards In Increasing Order.py

deck = [1,2,3,4,5,6,7,8,9,10]

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        n = len(deck)
        list1 = [i for i in range(n)]

        list2 = []
        count = 0
        while list1:
            if count % 2 == 0:
                list2.append(list1.pop(0))
            else:
                list1.append(list1.pop(0))
            count += 1

        ans = [None] * n
        print("list2",list2)
        for i in range(n):
            ans[list2[i]] = deck[i]
        return ans


a = Solution()
q = a.deckRevealedIncreasing(deck)
print("q=",q)