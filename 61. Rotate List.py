#-*- coding:utf-8 -*-
#@Date   : 2018/9/21
#@Author : suyifan
#@File   : 61. Rotate List.py

import copy

class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

l1 = None
temp = ListNode(6)
temp.next = l1
l1 = temp
temp = ListNode(5)
temp.next = l1
l1 = temp
temp = ListNode(4)
temp.next = l1
l1 = temp
temp = ListNode(3)
temp.next = l1
l1 = temp
temp = ListNode(2)
temp.next = l1
l1 = temp
temp = ListNode(1)
temp.next = l1
l1 = temp


# temp = l1
# while temp != None:
#     print(temp.val,"->",end="")
#     temp = temp.next
# print()


#### 计算k长度取余数
#### 考虑空的情况
#### 考虑移动次数为链表长度整数倍
k = 2
k = 0

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None

        self.head = head
        rtype = None
        ###计算head长度
        length = 0


        temp = self.head
        while temp != None:
            temp = temp.next
            length += 1
        ## k取余
        k = k % length
        if k == 0:
            return head

        ### 取出前半部分为 new_probe,剩下后半部分为old_probe
        # old_probe = head
        new_probe = None
        count = 0
        while count < length - k:
            temp = ListNode(self.head.val)
            temp.next = new_probe
            new_probe = temp
            self.head = self.head.next
            count += 1

        ###检验并输出前半部分
        # temp_new = new_probe
        # print("temp_new = ",end="")
        # while temp_new != None:
        #     print(temp_new.val,"->",end="")
        #     temp_new = temp_new.next
        # print()


        #测试l1
        # temp_l1 = l1
        # print("temp_l1 = ",end="")
        # while temp_l1 != None:
        #     print(temp_l1.val,"->",end="")
        #     temp_l1 = temp_l1.next
        # print()

        ##输出后半部分
        # temp_old = old_probe
        # print("temp_old = ",end="")
        # while temp_old != None:
        #     print(temp_old.val,"->",end="")
        #     temp_old = temp_old.next
        # print()

        ###翻转前半部分
        before = new_probe
        after = None
        while before != None:
            temp = before.next
            before.next = after
            after = before
            before = temp
        new_probe = after

        ###插入前半部分
        # old_probe1 = copy.copy(old_probe)
        temp1 = self.head
        while temp1.next != None:
            temp1 = temp1.next
        temp1.next = new_probe
        rtype = temp1

        ###测试
        # old_probe1 = copy.copy(old_probe)
        # temp1 = self.head
        # print("head = ",end="")
        # while temp1 != None:
            # print(temp1.val,"->",end="")
            # temp1 = temp1.next
        # print("None")

        # while temp1.next != None:
        #     temp1 = temp1.next
        # temp1.next = new_probe
        # rtype = temp1


        # rtype = ListNode(new_probe)
        # rtype.next = old_probe
        return  self.head

a = Solution()
q = a.rotateRight(l1,k)

print("rtype=",end=" ")
while q != None:
    print(q.val,"->",end="")
    q = q.next


    #### 备份
# head = l1
# k = 2
# class Solution:
#     def rotateRight(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#
#         ###计算head长度
#         length = 0
#         temp = head
#         while temp != None:
#             temp = temp.next
#             length += 1
#
#         ### 取出前半部分为 new_probe,剩下后半部分为old_probe
#         old_probe = copy.deepcopy(l1)
#         new_probe = None
#         count = 0
#         while count < length - k:
#             temp = ListNode(old_probe.val)
#             temp.next = new_probe
#             new_probe = temp
#             old_probe = old_probe.next
#             count += 1
#
#         ###检验并输出前半部分
#         temp_new = new_probe
#         print("temp_new = ",end="")
#         while temp_new != None:
#             print(temp_new.val,"->",end="")
#             temp_new = temp_new.next
#         print()
#
#
#         #测试l1
#         # temp_l1 = l1
#         # print("temp_l1 = ",end="")
#         # while temp_l1 != None:
#         #     print(temp_l1.val,"->",end="")
#         #     temp_l1 = temp_l1.next
#         # print()
#
#         ##输出后半部分
#         # temp_old = old_probe
#         # print("temp_old = ",end="")
#         # while temp_old != None:
#         #     print(temp_old.val,"->",end="")
#         #     temp_old = temp_old.next
#         # print()
#
#         ###插入前半部分
#         # old_probe1 = copy.copy(old_probe)
#         temp1 = old_probe
#         while temp1.next != None:
#             temp1 = temp1.next
#         temp1.next = new_probe
#         rtype = temp1
#
#         ####测试
#         # old_probe1 = copy.copy(old_probe)
#         # temp1 = head
#         # print("head = ",end="")
#         # while temp1 != None:
#         #     print(temp1.val,"->",end="")
#         #     temp1 = temp1.next
#         # print("jieshu")
#         # while temp1.next != None:
#         #     temp1 = temp1.next
#         # temp1.next = new_probe
#         # rtype = temp1
#
#
#         # rtype = ListNode(new_probe)
#         # rtype.next = old_probe
#
#         return  rtype
#
# a = Solution()
# q = a.rotateRight(head,k)
#
# print("rtype=",end=" ")
# while q != None:
#     print(q.val,"->",end="")
#     q = q.next