#-*- coding:utf-8 -*-
#@Date   : 2018/9/15
#@Author : suyifan
#@File   : 237. Delete Node in a Linked List.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#### 读题"你将只被给定要求删除的节点"
#### 不是给完整的链表
#### 把这个节点删除了就好了
head = [4,5,1,9]
node = 5
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


a = Solution()
q = a.deleteNode(node)