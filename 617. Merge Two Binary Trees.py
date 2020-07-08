#-*- coding:utf-8 -*-
#@Date   : 2018/10/4
#@Author : suyifan
#@File   : 617. Merge Two Binary Trees.py




# class ListNode():
#     def __init__(self,x,left = None,right = None):
#         self.val = x
#         self.left = left
#         self.right = right
#
#
# temp = ListNode(5)
# l1 = ListNode(3,temp)
# temp = ListNode(2)
# l1 = ListNode(1,l1,temp)
# probe = l1
#
#
#
# class Solution():
#     def __init__(self):
#         self.rtype = ListNode(0)
#
#
#
#     def mergeTrees(self,t1,t2):
#         if not t1 :
#             return None
#         temp = ListNode(t1.val)
#         temp.left = t1.left
#         temp.right = t1.right
#         rtype = temp
#         # self.mergeTrees(t1.left,t2)
#         # self.mergeTrees(t1.right,t2)
#         # self.print1(rtype)
#         return rtype
#
#
# def print1(lq):
#     if not lq :
#         return None
#
#     print(lq.val,end="...")
#     print1(lq.left)
#     print1(lq.right)
#
# a = Solution()
# q = a.mergeTrees(probe,None)
# print1(q)



###################################################
class ListNode():
    def __init__(self,x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right


temp = ListNode(5)
l1 = ListNode(3,temp)
temp = ListNode(2)
l1 = ListNode(1,l1,temp)
probe = l1



class Solution():

    def __init__(self):
        self.rtype = ListNode(0)

    def mergeTrees(self, t1, t2):
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        rtype = ListNode(t1.val )
        rtype.left = ListNode(9)
        # rtype.next = None
        # self.left(t1.left,t2.left,rtype)
        # self.right(t1.right,t2.right,rtype)
        # self.print1(rtype)
        while rtype != None:
            print(rtype.val,end="^")
            rtype = rtype.left
        return rtype


def print1(lq):
    if not lq :
        return None

    print(lq.val,end="...")
    print1(lq.left)
    print1(lq.right)

a = Solution()
q = a.mergeTrees(probe,None)
print1(q)