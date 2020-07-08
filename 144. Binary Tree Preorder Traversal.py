#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 144. Binary Tree Preorder Traversal.py




class Solution:
    def __init__(self):
        self.rtype = []

    def preorderTraversal(self,root):
        # if root == None:
        #     return None
        if root != None:
            self.rtype.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.rtype


