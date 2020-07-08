#-*- coding:utf-8 -*-
#@Date   : 2018/9/15
#@Author : suyifan
#@File   : 206. Reverse Linked List.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = None
for i in range(10):
    temp = ListNode(i)
    temp.next = head
    head = temp

temp1 = head
while temp1 != None:
    print(temp1.val,end=",")
    temp1 = temp1.next
print()
print("---")


#### 把链表打印出来,最后一个添加到新链表第一个,直到结束
#### 想明白怎么创建新链表就可以了,这题没坑
#### 但是第一次做时候真的不好想啊

#### 本道题实际考查的是链表循环,等我学完了单边表和双链表之后再来补坑

#### 答案思路也就那么回事,无非就是把创建节点环节省去了



# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         temp = None
#
#         while head != None:
#             rtype = temp
#             temp = ListNode(head.val)
#             temp.next = rtype
#             head = head.next
#         rtype = temp
#
#         return rtype
#
# a = Solution()
# q = a.reverseList(head)
#
# while q != None:
#     print(q.val,end=",")
#     q = q.next



class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        old_probe = head
        new_probe = None
        while old_probe != None:
            temp = old_probe.next
            old_probe.next = new_probe
            new_probe = old_probe
            old_probe = temp

        return new_probe

a = Solution()
q = a.reverseList(head)

while q != None:
    print(q.val,end=",")
    q = q.next