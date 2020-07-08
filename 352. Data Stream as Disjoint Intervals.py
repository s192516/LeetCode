#-*- coding:utf-8 -*-
#@Date   : 2019/1/12
#@Author : suyifan
#@File   : 352. Data Stream as Disjoint Intervals.py









# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        # self.n = 0
    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(Interval(val,val))
            # self.n += 1
        else:
            have = False
            if self.stack[0].start - 1 == val:
                self.stack[0].start -= 1
                have = True
            elif self.stack[0].start - 1 > val:
                self.stack.insert(0, Interval(val, val))
                have = True

            elif self.stack[-1].end + 1 == val:
                self.stack[-1].end += 1
                have = True

            elif self.stack[-1].end + 1 < val:
                self.stack.append(Interval(val, val))
                have = True

            if not have:
                for i,num in enumerate(self.stack):
                    if num.start - 1 == val:
                        if i != 0 and self.stack[i-1].end + 2 == num.start:
                            self.stack[i-1].end = num.end
                            self.stack.pop(i)
                            # self.n -= 1
                            break
                        else:
                            num.start -= 1
                    elif  num.end + 1 == val:
                        if len(self.stack)-1 != i and self.stack[i+1].start-2 == num.end:
                            num.end = self.stack[i+1].end
                            self.stack.pop(i+1)
                            # self.n -= 1
                            break
                        else:
                            num.end += 1
                    elif num.start - 1 == val:
                        print(val)
                        num.start -= 1
                        break
                    elif num.end + 1 == val  :
                        num.end += 1
                        break
                    elif i !=0 and (num.start > val and self.stack[i-1].end < val) :
                        self.stack.insert(i,Interval(val,val))




    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.stack


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

a = SummaryRanges()
list1 = ["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]

list2 = [[],[1],[],[3],[],[7],[],[2],[],[6],[]]
for i in range(len(list1)) :
    if list1[i] == "addNum":
        # print(type(list2[i][0]))
        a.addNum(list2[i][0])
    else:
        q = a.getIntervals()
        for i in q:
            print(i.start,i.end,end=" ")
        print()
        # print(a.getIntervals())
