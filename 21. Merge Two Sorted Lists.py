#-*- coding:utf-8 -*-
#@Date   : 2018/9/15
#@Author : suyifan
#@File   : 21. Merge Two Sorted Lists.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = l2 = None
for i in range(20,0,-2):
    temp = ListNode(i)
    temp.next = l1
    l1 = temp

for i in range(9,0,-2):
    temp = ListNode(i)
    temp.next = l2
    l2 = temp

temp1 = l1
while temp1 != None:
    print(temp1.val,end=",")
    temp1 = temp1.next
print()
temp1 = l2
while temp1 != None:
    print(temp1.val,end=",")
    temp1 = temp1.next
print("以上为测试")


##### 方向反了
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         rtype = ListNode("啦啦啦")
#         index_l1 = index_l2 = 0
#         while l1 != None and l2 != None:
#             # if l1.val >= l2.val:
#             #     temp =
#             break
#
#
#
#
#         while l1 != None:
#             count = index_l1
#             probe = rtype
#
#             while probe.next != None and count > 0:
#                 count -= 1
#                 probe = probe.next
#
#             index_l1 += 1
#             temp = ListNode(l1.val)
#             temp.next = rtype
#             rtype = temp
#             l1 = l1.next
#
#         while l2 != None:
#             count = index_l2
#             probe = rtype
#
#             while probe.next != None and count > 0:
#                 count -= 1
#                 probe = probe.next
#
#             index_l2 += 1
#             temp = ListNode(l2.val)
#             temp.next = rtype
#             rtype = temp
#             l2 = l2.next
#
#         return rtype
#
# a = Solution()
# q = a.mergeTwoLists(l1,l2)
#
# # print(q == None,"===")
# while q != None:
#     print(q.val,end="-")
#     q = q.next




class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rtype = None
        index_l1 = index_l2 = 0
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp = ListNode(l1.val)
                temp.next = rtype
                rtype = temp
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                temp.next = rtype
                rtype = temp
                l2 = l2.next

        while l1 != None:
            temp = ListNode(l1.val)
            temp.next = rtype
            rtype = temp
            l1 = l1.next

        while l2 != None:
            temp = ListNode(l2.val)
            temp.next = rtype
            rtype = temp
            l2 = l2.next

#####上面生成了一个链表,接下来给她反转
##### 反转和 #206思路一样

        # probe = rtype
        # temp = None
        # while rtype != None:
        #     probe1    = temp
        #     temp = ListNode(rtype.val)
        #     temp.next = rtype
        #     rtype = rtype.next
        # return rtype

        old_probe = rtype
        new_probe = None

        # count = 0
        # while count < 5:
        while old_probe != None:

            temp = old_probe.next

            old_probe.next = new_probe
            new_probe = old_probe
            old_probe = temp
            # count += 1

        return new_probe

a = Solution()
q = a.mergeTwoLists(l1,l2)

# print(q == None,"===")
while q != None:
    print(q.val,end="-")
    q = q.next