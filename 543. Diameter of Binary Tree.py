#-*- coding:utf-8 -*-
#@Date   : 2018/10/13
#@Author : suyifan
#@File   : 543. Diameter of Binary Tree.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.left = 0
        self.right = 0
        self.max_count = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = right = 0
        count_left = self.solve(root.left, left + 1, right)
        left = right = 0
        count_right = self.solve(root.right, left, right + 1)
        # left = right = 0
        # right = self.solve(root,right)
        print(count_left, count_right)
        return max(count_left + count_right, 0)

    def solve(self, root, left, right):
        if not root:
            return left + right - 1

        left_part = self.solve(root.left, left + 1, right)
        right_part = self.solve(root.right, left, right + 1)
        print(left_part, right_part, root.val)

        # if left_part + right_part > self.max_count:
        #     print(left_part,right_part,root.val)
        #     self.max_count = left_part + right_part
        return max(left_part, right_part, left_part)





##### 提交的

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self):
        self.left = 0
        self.right = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = right = 0
        count_left = self.solve(root.left, left, right)
        left = right = 0
        count_right = self.solve(root.right, left, right)
        # left = right = 0
        # right = self.solve(root,right)
        return count_left + count_right

    def solve(self, root, left, right):
        if not root:
            return left + right

        left_part = self.solve(root.left, left + 1, right)
        right_part = self.solve(root.right, left, right + 1)
        return max(left_part, right_part)