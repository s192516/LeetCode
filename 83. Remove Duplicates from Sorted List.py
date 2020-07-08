#-*- coding:utf-8 -*-
#@Date   : 2018/9/9
#@Author : suyifan
#@File   : 83. Remove Duplicates from Sorted List.py



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = None
for i in range(6):
    a = ListNode(i)
    a.val = i
    a.next = head
    head = a
temp = head

while head != None:
    if temp.val ==4:
        temp = head.next
    else:
        temp = temp.next


# temp,head = head,temp

while temp != None:
    print(temp.val)
    temp = temp.next



print(head)










# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None




# head = [1,1,2,3,4,5,6,7]
#
# class Solution:
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         rtype = None
#         list1 = None
#         for i in range(len(head)-1,-1,-1):
#             temp = ListNode(i)
#             temp.val = head[i]
#             temp.next = list1
#             list1 = temp
#             # rtype = temp
#
#         # probe = list1
#         # while probe != None:
#         #     print(probe.val)
#         #     probe = probe.next
#
#
#
#         probe = list1
#
#
#
#         while probe != None :
#             # print((probe))
#             if probe.next != None:
#
#                 if probe.val != probe.next.val:
#                     print(probe.val)
#                     probe = probe.next
#                 else:
#                     if  probe.next.next :
#                         probe = probe.next.next
#                     else:
#                         probe = None
#
#             else :
#                 probe = probe.next
#                 return list1

        # return list1


# a = Solution()
# q = a.deleteDuplicates(head)
# print("q=",q)

# while q != None:
#     print(q.val)
#     q = q.next