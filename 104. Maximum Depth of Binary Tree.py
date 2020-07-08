#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 104. Maximum Depth of Binary Tree.py





class Solution():
    def maxDepth(self,root):
        if root != None:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            rtype = max(left,right)
            return rtype + 1
        return 0