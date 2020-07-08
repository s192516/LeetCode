#-*- coding:utf-8 -*-
#@Date   : 2018/9/21
#@Author : suyifan
#@File   : 2. Add Two Numbers.py


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = None
temp = ListNode(3)
temp.next = l1
l1 = temp
temp = ListNode(4)
temp.next = l1
l1 = temp
temp = ListNode(2)
temp.next = l1
l1 = temp
# temp = ListNode(4)
# temp.next = l1
# l1 = temp
# temp = ListNode(5)
# temp.next = l1
# l1 = temp
# temp = ListNode(6)
# temp.next = l1
# l1 = temp


l2 = None
temp = ListNode(4)
temp.next = l2
l2 = temp
temp = ListNode(6)
temp.next = l2
l2 = temp
temp = ListNode(5)
temp.next = l2
l2 = temp
# temp = ListNode(4)
# temp.next = l2
# l2 = temp
# # temp = ListNode(5)
# temp.next = l2
# l2 = temp
# temp = ListNode(6)
# temp.next = l2
# l2 = temp

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        probe1 = l1
        probe2 = l2
        rtype = None
        jinwei = 0
        while probe1 != None and probe2 != None:
            val = probe1.val + probe2.val
            temp = ListNode((val + jinwei) % 10)
            if val + jinwei > 9:
                jinwei = 1
            else :
                jinwei = 0
            temp.next = rtype
            rtype = temp
            probe1 = probe1.next
            probe2 = probe2.next

        while  probe1 != None:
            temp = ListNode((probe1.val + jinwei) % 10)
            if probe1.val + jinwei > 9:
                jinwei = 1
            else:
                jinwei = 0
            temp.next = rtype
            rtype = temp
            probe1 = probe1.next



        while  probe2 != None:
            temp = ListNode((probe2.val + jinwei) % 10)
            if probe2.val + jinwei > 9:
                jinwei = 1
            else:
                jinwei = 0
            temp.next = rtype
            rtype = temp
            probe2 = probe2.next


        if jinwei != 0:
            temp = ListNode(1)
            temp.next = rtype
            rtype = temp


        old_probe = rtype
        new_probe = None
        # idx = None
        while old_probe != None:
            temp = old_probe.next
            old_probe.next = new_probe
            new_probe = old_probe
            old_probe = temp
        rtype = new_probe

        return rtype




a = Solution()
q = a.addTwoNumbers(l1,l2)

# print("q=",q)

while q != None:
    print(q.val,end="->")
    q = q.next