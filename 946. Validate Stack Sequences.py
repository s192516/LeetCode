#-*- coding:utf-8 -*-
#@Date   : 2018/11/25
#@Author : suyifan
#@File   : 946. Validate Stack Sequences.py

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]

pushed = [2,3,0,1]
popped = [0,3,2,1]


class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) != len(popped):
            return False
        stack = []
        for i in pushed:
            if i == popped[0]:
                popped.pop(0)
            else:
                while stack and stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)

                stack.append(i)
                # else:
                #     return False
        while stack:
            if stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            else:
                return False

        if not stack and not popped:
            return True
        else:
            return False

a = Solution()
q = a.validateStackSequences(pushed,popped)
print("q =",q)