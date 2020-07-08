#-*- coding:utf-8 -*-
#@Date   : 2018/10/9
#@Author : suyifan
#@File   : 148. Sort List.py




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # probe = head
        if head == None or head.next == None:
            return head

        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None
        return self.merge_sort(self.sortList(left), self.sortList(right),head)

    def merge_sort(self, left, right,head):
        temp = ListNode(0)
        # temp = head
        h = temp
        while left != None and right != None:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next

        if left != None:
            h.next = left
        if right != None:
            h.next = right
        return temp.next

    def get_mid(self, probe):
        fast = probe
        slow = probe
        ########你妈 这里应该是while 我怎么就给写成了if 得他妈多走多少次循环呐
        ########结果结果竟然是正确的我也是日了狗了
        ########!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow