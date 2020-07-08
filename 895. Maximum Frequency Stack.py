#-*- coding:utf-8 -*-
#@Date   : 2018/12/4
#@Author : suyifan
#@File   : 895. Maximum Frequency Stack.py

["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]

class FreqStack:
    def __init__(self):
        import collections
        self.freq = collections.Counter
        self.group = collections.defaultdict(list)
        self.max_freq = 0
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        n = self.freq[x]
        self.freq[x] = n + 1
        if n+1 > self.max_freq:
            self.max_freq = n+1
        self.group[n+1].append(x)



    def pop(self):
        """
        :rtype: int
        """
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()