# 92. https://leetcode.com/problems/reverse-linked-list-ii/

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # def reverseBetween(self, head, s_length, p_length):
    #     """
    #     :type head: ListNode
    #     :type s_length: int
    #     :type p_length: int
    #     :rtype: ListNode
    #     """
    #     count = 1
    #     root = ListNode(0)
    #     root.next = head
    #     pre = root
    #     while pre.next and count < s_length:
    #         pre = pre.next
    #         count += 1
    #     if count < s_length:
    #         return head
    #     mNode = pre.next
    #     curr = mNode.next
    #     while curr and count < p_length:
    #         next = curr.next
    #         curr.next = pre.next
    #         pre.next = curr
    #         mNode.next = next
    #         curr = next
    #         count += 1
    #     return root.next

    def reverseBetween(self, head, left, right):
        # creste a node dummy before the head
        dummy = ListNode(0, head)

        # initialize current node as head, prev node as dummy
        left_prev = dummy
        cur = head
        
        # 1. reach node at left point
        for i in range(1, left):
            left_prev = cur
            cur = cur.next

        # 2. reverse nodes from left point to right point
        new_head = None
        for i in range(left, right + 1):
            temp = cur.next
            cur.next = new_head
            new_head = cur
            cur = temp

        # 3. update pointers, connect nodes from left part to reversed part
        left_prev.next.next = cur
        left_prev.next = new_head
        return dummy.next