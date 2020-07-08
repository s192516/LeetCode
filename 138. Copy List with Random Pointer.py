#-*- coding:utf-8 -*-
#@Date   : 2018/11/3
#@Author : suyifan
#@File   : 138. Copy List with Random Pointer.py


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


#######第一段  ######还是看不懂那里错了


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        # 正确的第一步
        # p = head
        # while p:
        #     newNode = RandomListNode(p.label)
        #     newNode.next = p.next
        #     #newNode.random = None
        #     p.next = newNode
        #     p = p.next.next

        # 第一段######还是看不懂那里错了 #TODO
        probe = head
        while probe:
            temp = probe.next
            probe.next = RandomListNode(probe.label)
            probe = probe.next
            probe.next = temp
            probe = probe.next

        # #正确的第二步
        #         p = head
        #         while p:
        #             if p.random:
        #                 p.next.random = p.random.next
        #             p = p.next.next

        p = head
        newList = p.next
        while p:
            p_next = p.next
            p.next = p_next.next
            if p_next.next:
                p_next.next = p_next.next.next
            else:
                p_next.next = None
            p = p.next
        return newList