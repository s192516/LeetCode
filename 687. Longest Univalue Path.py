#-*- coding:utf-8 -*-
#@Date   : 2018/10/8
#@Author : suyifan
#@File   : 687. Longest Univalue Path.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.i = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        rtype = 0
        temp = 0

        rtype = self.solve(root)
        return self.i

    def solve(self, root):
        if not root:
            return self.i

        left = self.solve(root.left)
        right = self.solve(root.right)

        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0

        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0

        if self.i < left + right:
            self.i = left + right

        if left > right:
            return left
        else:
            return right
        # return rtype



