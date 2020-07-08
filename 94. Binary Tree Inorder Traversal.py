#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 94. Binary Tree Inorder Traversal.py




class Solution():
    def __init__(self):
        self.rtype = []

    def inorderTraversal(self,root):

        if root != None:
            self.inorderTraversal(root.left)
            self.rtype.append(root.val)
            self.inorderTraversal(root.right)
        return self.rtype