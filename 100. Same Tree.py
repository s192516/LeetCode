#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 100. Same Tree.py






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if q == None and p == None:
            return True
        if p != None and q != None and q.val == p.val:
            return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))
        else:
            return False
