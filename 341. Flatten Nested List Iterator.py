#-*- coding:utf-8 -*-
#@Date   : 2018/11/11
#@Author : suyifan
#@File   : 341. Flatten Nested List Iterator.py


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

nestedList = [0,[1,[2]]]

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        # for item in nestedList:
        while nestedList:
            item = nestedList.pop(0)
            if type(item) == list:
                nestedList += item
                # print(nestedList,"yes")
            else:
                # print(self.stack)
                self.stack.append(item)

        print(self.stack)
        self.n = len(self.stack) - 1

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

a = NestedIterator(nestedList)