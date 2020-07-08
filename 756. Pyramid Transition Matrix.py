#-*- coding:utf-8 -*-
#@Date   : 2019/1/9
#@Author : suyifan
#@File   : 756. Pyramid Transition Matrix.py


bottom = "ABC"
allowed = ["ABD","BCE","DEF","FFF"]
class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        import collections

        set_end = set()
        for word in allowed:
            set_end.add(word[-1])
        dict1 = collections.defaultdict(list)
        for word in allowed:
            dict1[word[-1]].append(word)
        print(dict1)
        while set_end:
            temp = []
            c = set_end.pop()
            if len(c) < len(bottom):
                c = c[1:]

a = Solution()
q = a.pyramidTransition(bottom,allowed)
print("q =",q)

sorted()