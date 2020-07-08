#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 101. Symmetric Tree.py



def Symmetric_Tree(self,root):
    if root == None :
        return True

    return self.solve(root.left,root.right)
def solve(self,left,right):
    if left == None and right == None:
        return True
    if left != None and right != None and left.val == right.val:

        return (self.solve(left.left, right.right) and self.solve(left.right, right.left))
    else:
        return False
